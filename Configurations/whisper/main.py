from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import subprocess
import os
import tempfile
import whisper
import asyncio
import logging

app = FastAPI()
model = whisper.load_model("base")  # You can change to "medium", "large", etc.

logging.basicConfig(level=logging.INFO)

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1] or ".webm"
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(await file.read())
        input_path = tmp.name

    chunk_dir = tempfile.mkdtemp()
    chunk_pattern = os.path.join(chunk_dir, "chunk_%03d.wav")

    try:
        split_command = [
            "ffmpeg", "-i", input_path,
            "-f", "segment",
            "-segment_time", "30",
            "-c:a", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            chunk_pattern
        ]
        result = subprocess.run(split_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            logging.error(f"FFmpeg failed with error:\n{result.stderr}")
            raise HTTPException(status_code=500, detail="Error processing audio file with ffmpeg")

        full_transcription = ""

        chunk_files = sorted(os.listdir(chunk_dir))
        for chunk_file in chunk_files:
            chunk_path = os.path.join(chunk_dir, chunk_file)
            transcription_result = await asyncio.to_thread(model.transcribe, chunk_path)
            full_transcription += transcription_result["text"] + " "

        return JSONResponse(content={"transcription": full_transcription.strip()})

    except Exception as e:
        logging.exception("Error during transcription")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.remove(input_path)
        for f in os.listdir(chunk_dir):
            os.remove(os.path.join(chunk_dir, f))
        os.rmdir(chunk_dir)
