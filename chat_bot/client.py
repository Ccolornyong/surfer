import os
import re

import openai

# env 파일 불러오기
from dotenv import load_dotenv

load_dotenv()

# 세팅
OPEN_KEY = os.getenv("OPEN_KEY")
MODEL = "gpt-4o-mini-2024-07-18"

openai.api_key = OPEN_KEY

# 프롬프트 작성 
def post_gpt(system_content, user_content):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ],
            max_tokens=500,
            stop=None,
            temperature=0.5
        )
        answer = response.choices[0].message.content
        print("gpt 답변: " + answer)
        return answer
    except Exception as e:
        print(e)
        return None
    
print(OPEN_KEY)
        
def create_prediction_prompt(prompt):
    system_content = "You are a helpful consulting assistant."
    pre_prompt = "친구가 되어서 함께 문자하는 것 처럼 답장해줘"
    answer = post_gpt(system_content, pre_prompt + prompt)
    return answer