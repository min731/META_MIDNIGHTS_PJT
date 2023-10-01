from typing import Union
import pickle

from fastapi import FastAPI, UploadFile
from models.openai_api import OpenAIChat
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse

from models.get_contents import GetContents
from typing import Any


app = FastAPI()
openai_chatbot = OpenAIChat()
get_contents = GetContents()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/answer")
def read_item99(idq: Union[str, None] = None, contentq: Any = None):
    # result = openai_chatbot.get_answer(content)
    print(type(contentq))
    print('=============================')

    content =   {"items": [{"id": idq, "content": contentq}]}
    print(content)
    return JSONResponse(content=content)


@app.post("/answer_")
def read_item(id: Union[str, None] = None, content: Union[str, None] = None):
    print(id)
    print(content)
    with open('instruments_contents/instruments_content.pickle', 'rb') as f:
        instruments_contents = pickle.load(f)

    all_instruments = instruments_contents.keys()
    
    req_instruments = get_contents.get_instruments(content)
    correct_text = get_contents.get_correct_text(content)

    input_ = '' + correct_text
    for req_instrument in req_instruments:
        input_ += req_instrument+'에 대한 설명이야.'+instruments_contents[req_instrument]

    result = openai_chatbot.get_answer(input_)

    content =   {"items": [{"id": id, "content": result}]}
    print(content)
    return JSONResponse(content=content)


@app.post("/send_sound")
def read_item(id: Union[str, None] = None, content: Union[str, None] = None):
    # result = openai_chatbot.get_answer(content)

    content =   {"items": [{"id": id, "content": content}]}
    print(content)
    filename = 'resource/test.wav'
    return FileResponse(filename, media_type="audio/wav", filename=filename)

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    print(file.filename)
    filename = 'resource/test.wav'
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    return FileResponse(filename, media_type="audio/wav", filename=filename)