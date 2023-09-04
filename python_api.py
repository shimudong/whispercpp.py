from fastapi import FastAPI, File, UploadFile
import uvicorn, json, datetime
import torch

from whispercpp import Whisper
model = Whisper('large')

app = FastAPI()

@app.post("/")
async def convert_audio_to_text(file: bytes = File(..., max_length=2097152)):
    global model
    with open("./wav_file/get.wav", 'wb') as f:
        f.write(file)

    result = model.transcribe("./wav_file/get.wav")
    text = model.extract_text(result)

    res = {
        "text": text,
    }
    
    return res

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=11111, workers=1)