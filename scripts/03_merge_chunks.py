import os
import math
import json

# number of chunks to combine in one group
n = 5

# loop through all files inside folder "data/processed/transcripts"
for filename in os.listdir("data/processed/transcripts"):

    if filename.endswith(".json"):

        file_path = os.path.join("data/processed/transcripts", filename)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            new_chunks = []  

            num_chunks = len(data['chunks'])

            num_group = math.ceil(num_chunks / n)

            for i in range(num_group):

                start_idx = i * n

                end_idx = min((i + 1) * n, num_chunks)

                chunk_group = data['chunks'][start_idx:end_idx]

                # create a new merged chunk
                new_chunks.append({
                    "number": data['chunks'][0]['number'],
                    "title": chunk_group[0]['title'],
                    "start": chunk_group[0]['start'],
                    "end": chunk_group[-1]['end'],
                    "text": " ".join(c['text'] for c in chunk_group)
                })

        os.makedirs("data/processed/chunks", exist_ok=True)

        with open(os.path.join("data/processed/chunks", filename), "w", encoding="utf-8") as json_file:
            json.dump({
                "chunks": new_chunks,
                "text": data['text']
            }, json_file, indent=4)