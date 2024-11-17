```py
db = FAISS.from_documents(docs, hf)

query = "인공지능 사업구조의 생김세는?"
docs = db.similarity_search(query)
print(docs[1].page_content)
```

```py
db.save_local("faiss_index")

new_db = FAISS.load_local("faiss_index", hf)
```

### 질문과 유사도 있는 서치 (vectorstore 필요)
```py
docs3 = db.similarity_search_with_relevance_scores(query, k=5)

print("질문:{} \n".format(query))
for i in range(len(docs3)):
    print("{0}유사도 \n{1}".format(i+1,round(docs3[i][1],2)))
    print("-"*100)
    print(docs3[i][0].page_content)
    print("\n")
    print(docs3[i][0].metadata)
    print("-"*100)
```


### 질문에 대한 다양성 서치 (vectorstore 필요)
```py
docs4 = db.max_marginal_relevance_search(query, k=5)

print("질문:{} \n".format(query))
for i in range(len(docs4)):
    print("{}유사도 문서".format(i+1))
    print("-"*100)
    print(docs4[i].page_content)
    print("\n")
    print(docs4[i].metadata)
    print("-"*100)
```

### 낮은수록 좋음 (vectorstore 필요)
```py
docs_and_scores = db.similarity_search_with_score(query)
print(docs_and_scores)
```