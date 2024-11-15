### FAISS + BM25 

```py
import faiss
from langchain_community.vectorstores import FAISS
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.prompts import PromptTemplate


# FAISS VectorStore 생성
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# FAISS에서 문서 임베딩 생성, FAISS retriever 생성
faiss_vectorstore = FAISS.from_documents(documents=splits_RCTS, embedding=embedding)
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})

# BM25 retriever 생성
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

# EnsembleRetriever 생성 (FAISS와 BM25 결과를 결합)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever], weight=[0.5, 0.5]
)

# 이제 ensemble_retriever를 사용하여 RAG 체인에서 검색을 실행할 수 있습니다.

```

### Chroma + BM25
```py
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.vectorstores import Chroma 

bm25_retriever = BM25Retriever.from_documents(docs)
bm25_retriever.k = 2

chroma_vector = Chroma.from_documents(docs, hf)
chroma_retriever = chroma_vector.as_retriever(search_kwargs={'k':2})


ensemble_retriever = EnsembleRetriever(
                    retrievers = [bm25_retriever,chroma_retriever]
                    , weight = {0.5,0.5})
```

### FAISS + Chroma + BM25
```py
import chromadb
from langchain_community.vectorstores import Chroma, FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# Chroma 클라이언트 설정
client = chromadb.Client()

# 문서 리스트 준비
doc_list = [split.page_content for split in splits_RCTS]

# Chroma VectorStore 생성
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# Chroma에서 문서 임베딩 생성
chroma_vectorstore = Chroma.from_documents(documents=splits_RCTS, embedding=embedding, client=client)

# FAISS VectorStore 생성
faiss_vectorstore = FAISS.from_documents(documents=splits_RCTS, embedding=embedding)

# BM25 retriever 생성
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

# Chroma retriever 생성
chroma_retriever = chroma_vectorstore.as_retriever(search_kwargs={"k": 2})

# FAISS retriever 생성
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})

# EnsembleRetriever 생성 (Chroma, FAISS, BM25 결과 결합)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, chroma_retriever, faiss_retriever],
    weight=[0.33, 0.33, 0.33]  # 세 가지 retriever의 결과를 동일한 비율로 결합
)
```