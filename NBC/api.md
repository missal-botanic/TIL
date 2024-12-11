
### Simple
```py
from dotenv import load_dotenv

# .env 파일 로드 (파일 경로는 실제 경로에 맞게 수정)
load_dotenv('/home/pro/VS/key.env')
```
### Kind
```py
import os
from dotenv import load_dotenv

# .env 파일 로드 (파일 경로는 실제 경로에 맞게 수정)
dotenv_path = '/home/pro/VS/key.env'  # .env 파일 경로
load_dotenv(dotenv_path=dotenv_path)

# 환경 변수에서 OpenAI API 키를 가져옴
api_key = os.getenv("OPENAI_API_KEY")

# 확인을 위해 API 키 출력 (보안상 실제 환경에서는 출력하지 않는 것이 좋습니다)
if api_key:
    print("API 키가 성공적으로 로드되었습니다.")
else:
    print("API 키를 .env 파일에서 찾을 수 없습니다.")

# 이제 API 키를 환경 변수로 설정하여 사용할 수 있습니다.
os.environ["OPENAI_API_KEY"] = api_key

# 예시로 OpenAI API를 사용하는 코드 작성 가능
```