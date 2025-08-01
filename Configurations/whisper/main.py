from fastapi import FastAPI, UploadFile, File, HTTPException
import subprocess
import os
import tempfile
import whisper
import asyncio

app = FastAPI()
model = whisper.load_model("base")  # Or "medium", "large", etc.

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1] or ".mp3"
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(await file.read())
        input_path = tmp.name

    chunk_dir = tempfile.mkdtemp()
    chunk_pattern = os.path.join(chunk_dir, "chunk_%03d.wav") 

    try:
        # Split into 30-second chunks using ffmpeg
        split_command = [
            "ffmpeg", "-i", input_path,
            "-f", "segment",
            "-segment_time", "30",
            "-c:a", "pcm_s16le",
            "-ar", "16000",   
            "-ac", "1",
            chunk_pattern
        ]
        subprocess.run(split_command, check=True)

        # Transcribe each chunk using Whisper asynchronously
        full_transcription = ""

        chunk_files = sorted(os.listdir(chunk_dir))
        for chunk_file in chunk_files:
            chunk_path = os.path.join(chunk_dir, chunk_file)
            result = await asyncio.to_thread(model.transcribe, chunk_path)
            full_transcription += result["text"] + " "

        return {"transcription": full_transcription.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
        for f in os.listdir(chunk_dir):
            os.remove(os.path.join(chunk_dir, f))
        os.rmdir(chunk_dir)
