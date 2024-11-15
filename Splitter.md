### CharacterTextSplitter
```py
# CharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

splits_CTS = text_splitter.split_documents(docs)
```

### RecursiveCharacterTextSplitter
```py
# RecursiveCharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

splits_RCTS = recursive_text_splitter.split_documents(docs)
```
### RecursiveCharacterTextSplitter + tiktoken
```py
# tiktoken 라이브러리와 langchain의 RecursiveCharacterTextSplitter 임포트
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 'cl100k_base' 토크나이저를 가져옴 (OpenAI GPT 모델용)
tokenizer = tiktoken.get_encoding("cl100k_base")

# tiktoken을 사용하여 텍스트의 토큰 길이를 계산하는 함수 정의
def tiktoken_len(text):
    # 입력된 텍스트를 'cl100k_base' 토크나이저로 인코딩하여 토큰으로 변환
    tokens = tokenizer.encode(text)
    # 토큰의 개수를 반환
    return len(tokens)

# 텍스트 분할기 설정
recursive_text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0, length_function = tiktoken_len)
# 페이지를 500자씩 분할하고, 중복되는 텍스트가 없도록 설정
splits_RCTS = recursive_text_splitter.split_documents(docs)  # 분할된 텍스트를 docs 변수에 저장
```


# Document 객체의 page_content 속성에서 텍스트의 길이를 측정
char_list = []
for i in range(len(splits_RCTS)):
    char_list.append(len(splits_RCTS[i].page_content))
print("chunk_size:")
print(char_list[:20])
print("="*100)

# 상위 50개 청크 선택
top_50_chunks_RCTS = splits_RCTS[:50]  # 순차적으로 상위 50개 청크 선택

# 상위 50개 청크 출력
for i, chunk in enumerate(top_50_chunks_RCTS):
    print(f"Chunk {i + 1}: {chunk}")