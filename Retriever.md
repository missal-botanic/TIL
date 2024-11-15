
```py
import faiss
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(documents=splits_RCTS, embedding=embeddings)

# RAG 체인에서 사용할 수 있도록 FAISS를 retriever로 변환하세요. 
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 1})




bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

embedding = OpenAIEmbeddings()
faiss_vectorstore = FAISS.from_texts(doc_list, embedding)
faiss_retriever = fasiss_vectorstore.as_retriever(search_kwargs={"k": 2})

ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever], weight=[0.5, 0.5]
)



import faiss
from langchain_community.vectorstores import FAISS
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate


# 1. FAISS VectorStore 생성
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# FAISS에서 문서 임베딩 생성
faiss_vectorstore = FAISS.from_documents(documents=splits_RCTS, embedding=embedding)

# 2. FAISS retriever 생성
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. BM25 retriever 생성
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

# 4. EnsembleRetriever 생성 (FAISS와 BM25 결과를 결합)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever], weight=[0.5, 0.5]
)

# 이제 ensemble_retriever를 사용하여 RAG 체인에서 검색을 실행할 수 있습니다.

```


pip3 install chromadb tiktoken transformers sentence_transformers
### 심플
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

### 로컬 캐시 저장 + 유사도
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

# 불러오기, 동일한 persist_directory를 사용하여 Chroma 인스턴스 다시 생성 (이미 존재하는 DB에서 불러오기)
db = Chroma(persist_directory=persist_dir, embedding_function=hf)

# 쿼리(query)에 대해 가장 유사한 문서들을 검색
# k=5는 상위 5개의 유사한 문서를 반환하도록 지정
docs = db.similarity_search_with_relevance_scores(query, k=5)

print("가장 유사한 문서 : \n{}".format(docs[0][0].page_content))  # 첫 번째 문서의 내용
print("유사도 : \n{}".format(docs[0][1]))  # 첫 번째 문서의 유사도 점수
```


```py
for i, (doc, score) in enumerate(docs):
    print(f"Rank {i+1}:")
    print("가장 유사한 문서 : \n{}".format(doc.page_content))  # 각 문서의 내용 출력
    print("유사도 : \n{}".format(score))  # 해당 문서의 유사도 점수 출력
    print("=" * 80)  # 구분선 추가
```