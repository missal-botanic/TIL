```py
from langchain.retrievers import BM25Retriever

# BM25 retriever 생성
doc_list = [split.page_content for split in splits_RCTS_tiktoken]
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 3  # 상위 3개의 문서 반환

# 쿼리로 BM25 검색 수행
query = "인공지능 사업구조의 생김세는?"
docs = bm25_retriever.get_relevant_documents(query)

# 문서와 점수 출력
for doc in docs:
    print(f"Document: {doc.page_content}")
```