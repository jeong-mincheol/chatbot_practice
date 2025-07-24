from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# CORS 허용 (Vue와 통신 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 * 가능. 실제 서비스는 도메인 지정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 사용자 메시지를 받을 모델
class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    user_input = message.text

    # 간단한 챗봇 로직
    if "안녕" in user_input:
        response = "안녕하세요! 무엇을 도와드릴까요?"
    elif "이름" in user_input:
        response = "저는 FastAPI 챗봇이에요!"
    else:
        response = "죄송해요, 잘 이해하지 못했어요."

    return {"response": response}
