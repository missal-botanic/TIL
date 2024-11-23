# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import gemini  # GEMINI.py를 불러옵니다

app = FastAPI()

# 요청 모델 정의 (쿼리를 받기 위한 모델)
class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query(request: QueryRequest):
    # 요청에서 쿼리 텍스트를 가져옴
    query_text = request.query
    if not query_text:
        raise HTTPException(status_code=400, detail="Query is required")

    # GEMINI.py에서 정의된 generate_response 함수 호출
    try:
        result = gemini.generate_response(query_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

    # 결과를 반환
    return {"result": result}

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)