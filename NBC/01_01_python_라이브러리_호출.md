라이브러리 호출
=============

### 키 관리
```py
from dotenv import load_dotenv

key = load_dotenv(r"C:\Users\241011\Documents\key.env")
print(key)
```

% 대문자는 클래스
```py
from pprint import pprint
```

### as  별칭 까지 가능
```py
from sklean.linear_model import LinearRegression as LR
```

### PyTorch 및 필요한 라이브러리 임포트
```py
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
```

### 각 최소 단위
```py
import pandas as pd
import numpy as np #다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용
from pandas import DataFrame
```

### Scikit-learn
```py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

```

### StandardScaler
```py
from sklearn.preprocessing import StandardScaler
```
기능: 데이터의 표준화를 수행하는 클래스입니다.
용도: 특성(feature)의 평균을 0, 표준편차를 1로 조정하여 데이터의 스케일을 통일합니다. 이는 특히 거리 기반 알고리즘이나 선형 모델에서 성능을 향상시킬 수 있습니다.


### LogisticRegression
```py
from sklearn.linear_model import LogisticRegression
```
기능: 로지스틱 회귀(Logistic Regression) 모델을 생성하는 클래스입니다.
용도: 이진 분류 문제에 사용되며, 독립 변수와 종속 변수 간의 관계를 모델링합니다. 예를 들어, Titanic 데이터에서 승객의 생존 여부를 예측하는 데 사용할 수 있습니다.

### accuracy_score
```py
from sklearn.metrics import accuracy_score
```
기능: 모델의 정확도를 계산하는 함수입니다.
용도: 실제 클래스와 예측한 클래스 간의 일치 비율을 계산하여 모델의 성능을 평가합니다. 정확도는 (올바르게 예측한 샘플 수) / (전체 샘플 수)로 정의됩니다.

### classification_report
```py
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다

### classification_report
```py
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다.


### nltk (Natural Language Toolkit)
```py
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
```
자연어 처리를 위한 라이브러리로, 다양한 텍스트 처리 작업을 지원합니다. 텍스트 토큰화, 품사 태깅, 구문 분석, 감정 분석 등 다양한 NLP 작업을 수행할 수 있도록 도와줍니다.

print(sent_tokenize(text))  # 문장 단위로 분리
print(word_tokenize(text))   # 단어 단위로 분리

### TextBlob:
```py
from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['sentiment'] = df['content_c'].apply(get_sentiment)
```

간단한 API로 자연어 처리 기능을 제공하는 라이브러리입니다. 감정 분석, 명사구 추출, 번역 등 다양한 기능을 쉽게 사용할 수 있습니다. TextBlob 객체를 사용하면 텍스트에 대한 감정 분석이나 언어 처리 작업을 간편하게 수행할 수 있습니다.

### re (정규 표현식):
```py
import re
```
문자열에서 패턴을 검색하고 조작하기 위한 라이브러리로, 정규 표현식을 사용하여 텍스트에서 특정 패턴을 찾거나 대체, 분할하는 등의 작업을 수행할 수 있습니다. 예를 들어, 구두점 제거, 특정 문자 또는 숫자를 찾는 작업에 유용합니다.

### 단어 구름을 생성하는 클래스
```py
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

nltk.download('stopwords')

stopwords = set(STOPWORDS) # 기본 불용어 목록을 STOPWORDS로부터 가져와 set 형태로 저장합니다.
stopwords.update(['netflix', 'movie', 'show', 'time', 'app', 'series', 'phone']) #추가적으로 분석에서 제외할 단어를 update 메서드를 통해 추가합니다.
```
WordCloud: 단어 구름을 생성하는 클래스
STOPWORDS: 제외할 일반 단어 리스트
matplotlib.pyplot: 그래프를 그리기 위한 라이브러리

## 불용어
```py
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) # NLTK에서 제공하는 영어 불용어 목록을 가져와 set 형태로 저장합니다. 

```
stopwords: NLTK(Natural Language Toolkit) 라이브러리에서 제공하는 불용어 목록을 사용합니다.
word_tokenize: 문장을 단어 단위로 분리(tokenize)하는 함수입니다.

### kaggle
```py
kaggle datasets download -d <dataset-identifier> #데이터셋 다운로드
kaggle competitions download -c titanic # 타이타닉 데이터셋 다운로드

unzip titanic.zip # 다운로드된 파일 압축 해제
```