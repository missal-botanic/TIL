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

# FAISS VectorStore 생성
faiss_vectorstore = FAISS.from_documents(documents=splits_RCTS, embedding=embedding)

# Chroma에서 문서 임베딩 생성
chroma_vectorstore = Chroma.from_documents(documents=splits_RCTS, embedding=embedding, client=client)

# BM25 retriever 생성
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 3

# Chroma retriever 생성
chroma_retriever = chroma_vectorstore.as_retriever(search_kwargs={"k": 3})

# FAISS retriever 생성
faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 3})

# EnsembleRetriever 생성 (FAISS, Chroma, 결과 결합)
ensemble_01_retriever = EnsembleRetriever(
    retrievers = [faiss_retriever, chroma_retriever],
    weight = {0.5,0.5})

# EnsembleRetriever 생성 (FAISS, BM25 결과 결합)
ensemble_02_retriever = EnsembleRetriever(
    retrievers = [faiss_retriever, bm25_retriever],
    weight = {0.5,0.5})

# EnsembleRetriever 생성 (Chroma, BM25 결과 결합)
ensemble_03_retriever = EnsembleRetriever(
    retrievers = [chroma_retriever, bm25_retriever],
    weight = {0.5,0.5})

# EnsembleRetriever 생성 (Chroma, FAISS, BM25 결과 결합)
ensemble_04_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, chroma_retriever, faiss_retriever],
    weight=[0.33, 0.33, 0.33]  # 세 가지 retriever의 결과를 동일한 비율로 결합
)


# 검색 결과 문서를 가져옵니다.
query = "메타 인공지능"

faiss_result = faiss_retriever.invoke(query)
chroma_result = chroma_retriever.invoke(query)
bm25_result = bm25_retriever.invoke(query)
ensemble_01_result = ensemble_01_retriever.invoke(query)
ensemble_02_result = ensemble_02_retriever.invoke(query)
ensemble_03_result = ensemble_03_retriever.invoke(query)
ensemble_04_result = ensemble_04_retriever.invoke(query)

print("[FAISS Retriever]")
for doc in faiss_result:
    print(f"Content: {doc.page_content}")
    print()

print("[chroma_retriever]")
for doc in chroma_result:
    print(f"Content: {doc.page_content}")
    print()

print("[BM25 Retriever]")
for doc in bm25_result:
    print(f"Content: {doc.page_content}")
    print()

# 가져온 문서를 출력합니다.
print("[FAISS, Chroma Ensemble Retriever]")
for doc in ensemble_01_result:
    print(f"Content: {doc.page_content}")
    print()

print("[FAISS, BM25 Ensemble Retriever]")
for doc in ensemble_02_result:
    print(f"Content: {doc.page_content}")
    print()

print("[Chroma, BM25 Ensemble Retriever]")
for doc in ensemble_03_result:
    print(f"Content: {doc.page_content}")
    print()

print("[Chroma, FAISS, BM25 Ensemble Retriever]")
for doc in ensemble_04_result:
    print(f"Content: {doc.page_content}")
    print()
```