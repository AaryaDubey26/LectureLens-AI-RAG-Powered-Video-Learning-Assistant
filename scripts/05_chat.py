import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import requests
import numpy as np 
import joblib
from google import genai
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# The client automatically picks up the GEMINI_API_KEY from the environment
client = genai.Client()

# Embedding Function (UNCHANGED)
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "nomic-embed-text",  # bge-m3
        "input": text_list
    })

    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.2
        }
    )
    return response.text


# RAG PIPELINE 

df = joblib.load('data/vector_db/embeddings.joblib')

incoming_query = input("Ask a Question: ")

question_embedding = create_embedding([incoming_query])[0]

print(question_embedding)

similarities = cosine_similarity(
    np.vstack(df['embedding']),
    [question_embedding]
).flatten()

top_results = 8

max_indx = similarities.argsort()[::-1][0:top_results]

new_df = df.iloc[max_indx]

prompt = f"""
Here are video chunks containing video title, number, start time,
end time and text:

{new_df[['title','number','start','end','text']].to_json(orient="records")}

------------------------------------------------------------

User Question:
{incoming_query}

Instructions:
- Answer only using the provided chunks.
- Mention video number , video title and timestamp range in minutes .
- Do NOT calculate total duration.
- Do NOT guess or invent timestamps.
- If topic is not clearly found, say it is not available in the provided data.
- Answer naturally like a course guide.
- If multiple timestamp ranges are continuous or very close,
combine them into a single larger range.
Avoid listing too many small fragmented timestamps.
Provide a clean and user-friendly summary.
"""

# Ensure directory exists for logs/temp files
os.makedirs("data/processed", exist_ok=True)

with open("data/processed/prompt.txt","w") as f:
    f.write(prompt)

response = inference(prompt)

print(response)

with open("data/processed/response.txt","w") as f:
    f.write(response)

# for index, item in new_df.iterrows():
#     print(index,item["title"],item["number"],item["text"],item["start"],item["end"])