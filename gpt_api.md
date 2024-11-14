# 모델 초기화
```py
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini",max_tokens = 1000, temperature = 0) # temperature = 0 ~ 2 높을 수록 다양한 답변
```

# 타이핑 방식으로 출력
```py
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 

model = ChatOpenAI(model="gpt-4o-mini", 
                   callbacks=[StreamingStdOutCallbackHandler()], 
                   temperature = 0, # temperature = 0 ~ 2 높을 수록 다양한 답변
                   max_tokens = 1000
                  ) 

# streaming=True 추가시 실시간 타이핑 이후 전체 메세지 재출력
```

```py
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 1)

messages = [
    SystemMessage(
        content="너는 20년차 시니어 개발자야. 사용자의 질문에 매우 건방지게 대답해줘."
    ),
    HumanMessage(
        content="파이썬의 장점에 대해서 설명해줘."
    ),
]
response_langchain = chatgpt.invoke(messages)
#response_langchain # 설정값 같이 출력
response_langchain.content # 문장만 출력
```
