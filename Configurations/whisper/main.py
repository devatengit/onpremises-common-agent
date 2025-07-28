from fastapi import FastAPI, UploadFile, File
import whisper

app = FastAPI()
model = whisper.load_model("base")  # voit käyttää myös "medium", "large" jne.

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    with open("temp_audio.mp3", "wb") as f:
        f.write(await file.read())
    result = model.transcribe("temp_audio.mp3")
    return {"text": result["text"]}
