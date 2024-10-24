라이브러리
=============
### as 까지 가능
```
from sklean.linear_model import LinearRegression as LR
```
대문자는 클래스
as 가능 

### 각 최소 단위
```
import pandas as pd
from pandas import DataFrame
```


### numpy
```
import numpy as np
```

### pandas
```
import pandas as pd


df = pd.read_csv('data.csv') # CSV 파일 불러오기

df = pd.read_excel('data.xlsx', sheet_name='Sheet1') # 엑셀 파일 불러오기

print(df.head())

df.shape # 데이터 프레임의 크기 (행, 열) 확인


df.columns # 데이터 프레임의 컬럼명 확인


df.dtypes # 데이터 프레임의 데이터 타입 확인


df.describe() # 데이터 프레임의 요약 통계량 확인


df.info() # 데이터 프레임의 정보 확인 (null 값, 데이터 타입 등)

df = pd.DataFrame(data)
df["이름"][0]

```

### kaggle
```
pip install kaggle
kaggle datasets download -d <dataset-identifier> #데이터셋 다운로드

kaggle competitions download -c titanic # 타이타닉 데이터셋 다운로드

unzip titanic.zip # 다운로드된 파일 압축 해제
```


### PyTorch 및 필요한 라이브러리 임포트
```
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
```

데이터 분석을 위해 사용되는 라이브러리로, 주로 데이터프레임(dataframe) 형식으로 데이터를 처리하고 분석하는 데 사용됩니다. CSV 파일, 엑셀 파일 등 다양한 형식의 데이터를 쉽게 다룰 수 있습니다.
nltk (Natural Language Toolkit):

### train_test_split
```
from sklearn.model_selection import train_test_split
```
기능: 데이터를 학습용(train)과 테스트용(test)으로 나누는 함수입니다.
용도: 모델의 성능을 평가하기 위해 데이터를 두 개의 세트로 분리합니다. 일반적으로 test_size를 지정하여 테스트 세트의 비율을 설정합니다. 이를 통해 과적합(overfitting)을 방지할 수 있습니다.


### StandardScaler
```
from sklearn.preprocessing import StandardScaler
```
기능: 데이터의 표준화를 수행하는 클래스입니다.
용도: 특성(feature)의 평균을 0, 표준편차를 1로 조정하여 데이터의 스케일을 통일합니다. 이는 특히 거리 기반 알고리즘이나 선형 모델에서 성능을 향상시킬 수 있습니다.


### LogisticRegression
```
from sklearn.linear_model import LogisticRegression
```
기능: 로지스틱 회귀(Logistic Regression) 모델을 생성하는 클래스입니다.
용도: 이진 분류 문제에 사용되며, 독립 변수와 종속 변수 간의 관계를 모델링합니다. 예를 들어, Titanic 데이터에서 승객의 생존 여부를 예측하는 데 사용할 수 있습니다.

### accuracy_score
```
from sklearn.metrics import accuracy_score
```
기능: 모델의 정확도를 계산하는 함수입니다.
용도: 실제 클래스와 예측한 클래스 간의 일치 비율을 계산하여 모델의 성능을 평가합니다. 정확도는 (올바르게 예측한 샘플 수) / (전체 샘플 수)로 정의됩니다.

### classification_report
```
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다

### classification_report
```
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다.


### nltk (Natural Language Toolkit)
```
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
```
자연어 처리를 위한 라이브러리로, 다양한 텍스트 처리 작업을 지원합니다. 텍스트 토큰화, 품사 태깅, 구문 분석, 감정 분석 등 다양한 NLP 작업을 수행할 수 있도록 도와줍니다.


print(sent_tokenize(text))  # 문장 단위로 분리
print(word_tokenize(text))   # 단어 단위로 분리


### TextBlob:
```
from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['sentiment'] = df['content_c'].apply(get_sentiment)
```

간단한 API로 자연어 처리 기능을 제공하는 라이브러리입니다. 감정 분석, 명사구 추출, 번역 등 다양한 기능을 쉽게 사용할 수 있습니다. TextBlob 객체를 사용하면 텍스트에 대한 감정 분석이나 언어 처리 작업을 간편하게 수행할 수 있습니다.

### re (정규 표현식):
```
import re
```
문자열에서 패턴을 검색하고 조작하기 위한 라이브러리로, 정규 표현식을 사용하여 텍스트에서 특정 패턴을 찾거나 대체, 분할하는 등의 작업을 수행할 수 있습니다. 예를 들어, 구두점 제거, 특정 문자 또는 숫자를 찾는 작업에 유용합니다.

### 단어 구름을 생성하는 클래스
```
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
```
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) # NLTK에서 제공하는 영어 불용어 목록을 가져와 set 형태로 저장합니다. 

```
stopwords: NLTK(Natural Language Toolkit) 라이브러리에서 제공하는 불용어 목록을 사용합니다.
word_tokenize: 문장을 단어 단위로 분리(tokenize)하는 함수입니다.

