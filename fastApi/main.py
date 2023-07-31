from fastapi import FastAPI,UploadFile
import uuid, os
from typing import List 
from pydantic import BaseModel
# import face_recognition
# import cv2
# import dlib
# import imutils
# from imutils import face_utils
# import numpy as np
# import matplotlib.pyplot as plt

class TagImage(BaseModel):
    name: str
    img : UploadFile

app = FastAPI()

@app.get(path="/items/{item_id}",description="test api" )
async def root(item_id:int):
    return {"message" : "Hello World",
            "item_id" : item_id}


@app.post("/regist")
async def upload_photo(files: List[UploadFile], description="강아지 얼굴 등록하는 함수, json으로 강아지 이름과 사진을 받음"):
    upload_dir = f'{os.getcwd()}/data/img'
    os.makedirs(upload_dir,exist_ok=True)
    for file in files:
        content = await file.read()
        filename = f"{str(uuid.uuid4())}.jpg"
        with open(os.path.join(upload_dir,filename), "wb") as fp:
            fp.write(content)

    return {"filename" : [file.filename for file in files]}

@app.get("/getRegistedDogs", description="등록된 강아지 이름과 사진을 반환")
async def getAll_dogsInfo():
    return

@app.post("/check", description="강아지 사진을 전달해주면, 등록된 강아지 사진과 비교하여 일치 불일치 반환")
async def check_mydog():
    return 

@app.get("/flush",  description="등록된 강아지 정보 모두 날림")
async def eraseAll_registedIMG():
    return
