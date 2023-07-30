from fastapi import FastAPI
import cv2
import dlib
import imutils
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt
 
import face_recognition

app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id:int):
    return {"message" : "Hello World",
            "item_id" : item_id}


@app.post("/photo")
async def upload_photo(file: UploadFile):
    upload_dir = './data/img'

    content = await file.read()
    filename = f"{str(uuid.uuid4())}.jpg"
    with open(os.path.join(upload_dir, filename), "wb") as fp:
        fp.write(content)

    return {"filename" : filename}
