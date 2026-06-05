import requests
import os
import json
import pandas as pd
import numpy as np
import joblib


def create_embedding(text):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "nomic-embed-text",
        "input": text
    })

    embedding = r.json()['embeddings']
    return embedding

jsons = os.listdir("data/processed/chunks")
# print(jsons)
my_dicts = []
chunk_id=0

for json_files in jsons:
    with open(f"data/processed/chunks/{json_files}") as f:
        content = json.load(f)

    print(f"Creating Embedding for {json_files}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i,chunk in enumerate(content['chunks']):
        chunk['chunk_id']=chunk_id
        chunk['embedding']=embeddings[i]
        chunk_id+=1
        my_dicts.append(chunk)      
# print(my_dicts)

df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df,'data/vector_db/embeddings.joblib')