from fastapi import FastAPI, UploadFile, File
import subprocess
import os
import tempfile
import whisper

app = FastAPI()
model = whisper.load_model("base")  # Or "medium", "large", etc.

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        input_path = tmp.name

    # Output chunk directory
    chunk_dir = tempfile.mkdtemp()
    chunk_pattern = os.path.join(chunk_dir, "chunk_%03d.mp3")

    # Split into 30-second chunks
    split_command = [
        "ffmpeg", "-i", input_path,
        "-f", "segment",
        "-segment_time", "30",
        "-c", "copy",
        chunk_pattern
    ]
    subprocess.run(split_command, check=True)

    # Transcribe all chunks
    full_transcription = ""
    for chunk_file in sorted(os.listdir(chunk_dir)):
        chunk_path = os.path.join(chunk_dir, chunk_file)
        result = model.transcribe(chunk_path)
        full_transcription += result["text"] + " "

    # Clean up
    os.remove(input_path)
    for f in os.listdir(chunk_dir):
        os.remove(os.path.join(chunk_dir, f))
    os.rmdir(chunk_dir)

    return {"transcription": full_transcription.strip()}
