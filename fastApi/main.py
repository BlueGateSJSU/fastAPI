from fastapi import FastAPI,UploadFile
import uuid
# import cv2
# import dlib
# import imutils
# from imutils import face_utils
# import numpy as np
# import matplotlib.pyplot as plt
import os
from typing import List
# import face_recognition

app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id:int):
    return {"message" : "Hello World",
            "item_id" : item_id}


@app.post("/photo")
async def upload_photo(files: List[UploadFile]):
    upload_dir = f'{os.getcwd()}/data/img'
    os.makedirs(upload_dir,exist_ok=True)
    for file in files:
        content = await file.read()
        filename = f"{str(uuid.uuid4())}.jpg"
        # filename = f"{file.filename}.jpg"
        with open(os.path.join(upload_dir,filename), "wb") as fp:
            fp.write(content)

    return {"filename" : [file.filename for file in files]}
