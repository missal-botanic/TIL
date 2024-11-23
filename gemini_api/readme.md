### 3. FastAPI 실행

위의 `main.py` 코드에서 `FastAPI` 서버를 실행합니다. 서버가 실행되면, 사용자가 쿼리를 `POST` 방식으로 보낼 수 있습니다.

다음 명령어로 `Uvicorn` 서버를 실행할 수 있습니다:

```bash
uvicorn main:app --reload
```

이 명령어는 FastAPI 애플리케이션을 실행하고, `http://127.0.0.1:8000`에서 API를 사용할 수 있도록 합니다.

### 4. API 사용 예시

이제 클라이언트에서 FastAPI 서버에 `POST` 요청을 보내어 `GEMINI.py`에서 생성된 응답을 받을 수 있습니다. 예를 들어 `curl`을 사용하여 요청을 보내면 다음과 같습니다:

```bash
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "Explain how AI works"}'
```

응답 예시는 다음과 같이 생성된 텍스트가 포함됩니다:

```json
{
  "result": "AI works by processing large amounts of data, identifying patterns, and making predictions or decisions based on those patterns..."
}
```

파이썬으로 호출하는 예시입니다.

```py
import requests
import json

# 요청 URL
url = "http://127.0.0.1:8000/query"

# 요청에 보낼 데이터
data = {
    "query": "한글로 인공지능에 대해 설명해줘"
}

# POST 요청을 보내기 위한 헤더 설정
headers = {
    "Content-Type": "application/json"
}

# POST 요청 보내기
response = requests.post(url, json=data, headers=headers)

# 응답 출력
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
```

### 5. FastAPI 문서화

FastAPI는 자동으로 Swagger UI를 생성하여 API 문서를 제공합니다. `http://127.0.0.1:8000/docs`에서 이 문서와 인터페이스를 확인할 수 있습니다.