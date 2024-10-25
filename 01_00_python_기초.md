
### Pandas
기본은 행 axis=0 
X = df.drop('data') #는 열이기 떄문에 axis=1 자동 인식
X = df.drop('sdata', axis=1) #가독성을 위해 명시적으로 표시

### range 활용

'id': range(1, 201)

### print 기법
r2 = r2_score(y_te, pre_v) #작동
print(r2 = r2_score(y_te, pre_v)) #미작동
print(r2_score(y_te, pre_v)) #작동

### random number
```
import random
rn = random.random() # 괄호 안에는 아무것도 들어가지 못함
```
```
rn = random.random()
df['01'] = [rn for _ in range(100)] # 한번 생성된 값만 저장

df['01'] = [random.random() for _ in range(100)] # 매번 생성

df['01'] = [random.random() for i in range(100)] # 같은 결과
```


### model.fit(X,y)
X는 여러 특성(2D 배열): 여러 샘플과 여러 특성을 고려해야 하기 때문에 2D 배열 형식이 필요합니다.
y는 단일 결과(1D 배열): 각 샘플에 대해 하나의 목표 값만 필요하므로 1D 배열 형식이 필요합니다.

### lambda x:, 함수 (map(), apply(), filter(), sorted())

### ' '.join(...):

join 메서드는 문자열을 결합하는 데 사용됩니다.
' '.join(...)는 선택한 긍정적인 리뷰들을 공백을 구분자로 하여 하나의 긴 문자열로 결합합니다.
예를 들어, 긍정적인 리뷰가 ["Great movie!", "Loved it!", "Highly recommend!"]라면, 결과는 "Great movie! Loved it! Highly recommend!"와 같이 됩니다.

###  이미지를 부드럽게
```
plt.imshow(wordcloud, interpolation='bilinear')
```
###  순환돌리기 예시
result = []
for token in word_tokens: 
    if token not in stop_words: 
        result.append(token) 
```
def add_one(x):
    return x + 1 # 일반 함수

add_one_lambda = lambda x: x + 1 # 람다 함수

print(add_one(5))  # 출력: 6 # 일반 함수
print(add_one_lambda(5))  # 출력: 6 # 람다 함수
```


### 기본값은 오름 차순 ascending = False 내림차순으로


### print(not a)    # False

### x += 10
```
x = 10
x = x + 10
x
와 같다
```

### 길이가 같아야 한다

data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 35],
    '직업': ['학생', '회사원', '프리랜서']
}


### inpace= 영구 변환 그냥 set 한번 변환

### ~반대조건

### 복합 /= 은 안되도 a=a/n은 될 수 있다.

결측값 처리 : 누락된 값
이상값 처리 : 비상식적으로 큰 값이나 작은 값
중복 데이터 제거 : 동일한 테이터 
데이터 타입 변환 : 데이터 타입 변환
데이터 정규화 : 범위를 일정하게
인코딩 : 범주형을 수치형으로
샘플링 : 데이터 셋의 크기를 줄이거나 늘리기
특징 선택 및 추출 : 중요한 특징 선택 및 새로운 특징 추출

- 2) 데이터 전처리의 주요 기법
    
    **결측치 처리 (Handling Missing Data)**
    
    결측치는 데이터셋에 누락된 값을 의미합니다. 결측치를 처리하지 않으면 모델의 성능이 저하될 수 있습니다.
    
    삭제: 결측치가 있는 행이나 열을 삭제합니다. 결측치가 적을 때 유용하지만, 데이터 손실이 발생할 수 있습니다.
    대체: 평균, 중앙값, 최빈값 등으로 결측치를 대체합니다.
    예측: 다른 특성을 사용하여 결측치를 예측하고 채웁니다.
    
     **이상치 처리 (Handling Outliers)**
    
    이상치는 데이터에서 비정상적으로 크거나 작은 값을 의미합니다. 이상치는 모델의 성능을 저하시킬 수 있습니다.
    
    제거: 이상치를 데이터셋에서 제거합니다.
    변환: 이상치를 다른 값으로 변환합니다 (예: 상한선이나 하한선으로 대체).
    IQR 방법: IQR(Interquartile Range)을 사용하여 이상치를 탐지하고 처리합니다.
    
      **데이터 정규화 (Normalization)**
    
    정규화는 데이터를 일정한 범위로 스케일링하는 과정입니다. 일반적으로 [0, 1] 범위로 변환합니다.
    
   Min-Max 정규화: 최소값을 0, 최대값을 1로 변환합니다.
    $Xnorm=Xmax−XminX−Xmin$
        
        $Xnorm=X−XminXmax−XminX_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$
        
    
     **데이터 표준화 (Standardization)**
    
    표준화는 데이터를 평균 0, 분산 1로 변환하는 과정입니다.
    
    Z-점수 표준화: $Xstd=σX−μ$
    여기서 $\mu$는 평균, $\sigma$는 표준편차입니다.
        
        $Xstd=X−μσX_{std} = \frac{X - \mu}{\sigma}$
        
    
    **특성 공학 (Feature Engineering)**
    
    특성 공학은 데이터로부터 새로운 유용한 특성을 생성하는 과정입니다.
    
     특성 생성: 기존 데이터를 기반으로 새로운 특성을 생성합니다 (예: 날짜 데이터를 사용하여 요일 특성 생성).
     특성 선택: 모델 성능에 중요한 특성을 선택하고, 중요하지 않은 특성을 제거합니다.

    **데이터 인코딩 (Data Encoding)**
    
    비정형 데이터를 모델이 이해할 수 있는 형태로 변환합니다.
    
    레이블 인코딩 (Label Encoding): 범주형 데이터를 숫자로 변환합니다.
    원-핫 인코딩 (One-Hot Encoding): 범주형 데이터를 이진 벡터로 변환합니다.
    
     **데이터 분할 (Data Splitting)**
    
    데이터를 학습용(train), 검증용(validation), 테스트용(test)으로 분할합니다. 이를 통해 모델의 일반화 성능을 평가할 수 있습니다.
    
     학습 데이터 (Training Data): 모델 학습에 사용되는 데이터.
     검증 데이터 (Validation Data): 모델 튜닝 및 성능 검증에 사용되는 데이터.
     테스트 데이터 (Test Data): 최종 모델 평가에 사용되는 데이터.






비트연산자?
이터레이터?