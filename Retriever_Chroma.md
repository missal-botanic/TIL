


pip3 install chromadb tiktoken transformers sentence_transformers
### Chroma 심플
```py
from langchain.vectorstores import Chroma 

# 1. 문서들을 임베딩 후 Chroma DB에 저장, hf는 HuggingFace 임베딩 모델
db = Chroma.from_documents(docs, hf)  

# 2. 유사한 문서 검색: 주어진 쿼리(query)에 대해 벡터 DB에서 유사한 문서들을 검색
# 이때 유사도 점수는 포함되지 않음 (단순히 가장 유사한 문서만 반환)
docs = db.similarity_search(query) 

print(docs[0].page_content)  # 3.검색된 문서의 첫 번째 결과 출력 
print(tiktoken_len(docs[0].page_content)) # 검색된 문서의 길이 출력 (토큰 수 기준)
```

### Chroma 로컬 캐시 저장 + 유사도
```py
import os
from langchain.vectorstores import Chroma  

# 절대 경로로 Chroma DB 디렉토리 설정
persist_dir = os.path.abspath("/home/pro/VS/chroma_db/")  

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(persist_dir):
    os.makedirs(persist_dir)  # 디렉토리 생성

# 저장, Chroma 데이터베이스 생성 및 저장: docs는 이미 문서들에 대한 임베딩된 리스트입니다.
db = Chroma.from_documents(docs, hf, persist_directory=persist_dir)

# ==========================================================================

# 불러오기, 동일한 persist_directory를 사용하여 Chroma 인스턴스 다시 생성 (이미 존재하는 DB에서 불러오기)
db = Chroma(persist_directory=persist_dir, embedding_function=hf)

# 쿼리(query)에 대해 가장 유사한 문서들을 검색
# k=5는 상위 5개의 유사한 문서를 반환하도록 지정
docs = db.similarity_search_with_relevance_scores(query, k=5)

```


### 결과물
```py
docs = db3.similarity_search(query)
print("가장 유사한 문서 : \n{}".format(docs[0][0].page_content))  # 첫 번째 문서의 내용
print("유사도 : \n{}".format(docs[0][1]))  # 첫 번째 문서의 유사도 점수
```

### 결과물 + 유사도 출력
```py
docs = db3.similarity_search_with_relevance_scores(query, k=3)
for i, (doc, score) in enumerate(docs):
    print(f"Rank {i+1}:")
    print("가장 유사한 문서 : \n{}".format(doc.page_content))  # 각 문서의 내용 출력
    print("유사도 : \n{}".format(score))  # 해당 문서의 유사도 점수 출력
    print("=" * 80)  # 구분선 추가
```