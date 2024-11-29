```py

import google.generativeai as genai

# API 키 설정
key = "your_actual_api_key"  # 실제 API 키로 변경해야 합니다
genai.configure(api_key=key)

# 모델 인스턴스 생성
model = genai.GenerativeModel("gemini-1.5-flash")

# 사용자 쿼리
query = "Your question here"  # 사용자가 입력하는 질문

# 콘텐츠 생성
response = model.generate(query)

# 응답 출력
print(response)

```

```py
import google.generativeai as genai

# API 키 설정
api_key = "your_actual_api_key"  # 실제 API 키로 변경해야 합니다
genai.configure(api_key=api_key)

# Google Gemini 모델 인스턴스 생성 (함수 외부로 이동)
model = genai.GenerativeModel("gemini-1.5-flash")

# Google Gemini 모델을 통해 응답을 생성하는 함수
def generate_response(query: str) -> str:
    """
    주어진 쿼리를 바탕으로 Google Gemini 모델을 통해 응답을 생성하는 함수.
    """
    # 모델을 사용해 응답 생성
    response = model.generate_content(query)  # generate_content() 메소드 사용
    
    # 생성된 응답 텍스트 반환
    return response.text

```