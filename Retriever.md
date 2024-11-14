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

