# 긴 문맥 재정렬(LongContextReorder)
from langchain_community.document_transformers import LongContextReorder
reordering = LongContextReorder()
reordered_docs = reordering.transform_documents(docs)

# 4개의 관련 문서가 시작과 끝에 위치하는지 확인합니다.
reordered_docs