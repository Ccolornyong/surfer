import os
import re
import openai
from dotenv import load_dotenv

load_dotenv()

# 환경 변수 로드
OPEN_KEY = os.getenv("OPEN_KEY")
MODEL = "gpt-4o-mini-2024-07-18"

openai.api_key = OPEN_KEY

completion = openai.ChatCompletion.create(
    model = MODEL,
    messages = [
        {"role": "system", "content": "일반회계, 특별회계, 기금간의 차이는 무엇인가요? 한 문장으로 대답하세요."},
    ]
)

print(completion.choices[0].message['content'])