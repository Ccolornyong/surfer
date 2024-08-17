from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from chat_bot.yolov5.client import create_prediction_prompt  # client.py에서 임포트

app = FastAPI()

class RequestResumeScript(BaseModel):
    content: str

@app.get("/")
def read_root():
    return "FastAPI"

@app.post("/chat_bot")
def create_prediction_prompt_endpoint(data: RequestResumeScript):
    try:
        # client.py의 create_prediction_prompt 함수 호출
        content = create_prediction_prompt(data.content)
        if not content:
            raise HTTPException(status_code=204, detail="Something went wrong")
        
        response_data = {
            "status": 200,
            "data": content,
        }

    except HTTPException as e:
        response_data = {
            "status": e.status_code,
            "data": "죄송합니다. 오류로 인해 예상 질문이 생성되지 않았습니다. 다시 시도해주세요.",
        }

    return content


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000, reload=True, workers=1)
