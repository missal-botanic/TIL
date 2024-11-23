
import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env 파일에서 API 키 로딩
load_dotenv(r"C:\Users\241011\Documents\key.env")
key = os.getenv("GOOGLE_API_KEY")

if key:
    print("yes key")
else:
    print("no key")

# Google Generative AI 설정
genai.configure(api_key=key)

def generate_response(query: str) -> str:
    """
    주어진 쿼리를 바탕으로 Google Gemini 모델을 통해 응답을 생성하는 함수.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    return response.text