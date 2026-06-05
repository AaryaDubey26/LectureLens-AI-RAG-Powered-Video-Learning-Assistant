# converts the videos into mp3
import os
import subprocess

files = os.listdir("data/raw")

for file in files:

    tutorial_number = file.split(" #")[1].split(".")[0]
    file_name = file.split(" ｜ ")[0]

    print(tutorial_number, file_name)

    subprocess.run([
        "ffmpeg",
        "-i", f"data/raw/{file}",
        f"data/processed/audios/{tutorial_number}_{file_name}.mp3"
    ])