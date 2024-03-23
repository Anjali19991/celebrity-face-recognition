from fastapi import FastAPI, File
from artifacts.preprocessing import preprocessing

app = FastAPI()

@app.get("/")
def index():
    return {"Hello":"hello"}

@app.post("/get-image")
async def UploadImage(file: bytes = File(...)):
    with open('./artifacts/image.jpg','wb') as image:
        image.write(file)
        image.close()
    preprocessing('./artifacts/image.jpg')
    
    return 'got it'