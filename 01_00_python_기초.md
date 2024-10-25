python_기초
=============

### inpace= 영구 변환 그냥 set 한번 변환

### 복합 /= 은 안되도 a=a/n은 될 수 있다.

### map(), apply(), filter(), sorted()

### ~반대조건

### 일반 함수
```
def add_one(x):
    return x + 1 

```

### x += 10
```
x = 10
x = x + 10
x
와 같다
```

### 기본값
```
기본은 행 axis=0 
X = df.drop('data') #는 열이기 떄문에 axis=1 자동 인식
X = df.drop('sdata', axis=1) #가독성을 위해 명시적으로 표시
```

### range 활용
```
'id': range(1, 201)
```

### random number & for i range()
```
import random
rn = random.random() # 괄호 안에는 아무것도 들어가지 못함
```
```
rn = random.random()
df['01'] = [rn for _ in range(100)] # 한번 생성된 값만 저장

df['01'] = [random.random() for i in range(100)] # 매번 생성
df['01'] = [random.random() for _ in range(100)] # _ 사용하지 않음 의미

```

### print 기법
```
print(r2_score(y_te, pre_v)) #작동
r2 = r2_score(y_te, pre_v) #작동

print(r2 = r2_score(y_te, pre_v)) #미작동
```

### print(not a) 
```
a = True
print(not a)  # 출력: False

a = False
print(not a)  # 출력: True
```

### lambda x:, 함수 
```
add_one_lambda = lambda x: x + 1 # 람다 함수

print(add_one(5))  # 출력: 6 # 일반 함수
print(add_one_lambda(5))  # 출력: 6 # 람다 함수
```

### ' '.join(...):

join 메서드는 문자열을 결합하는 데 사용됩니다.
' '.join(...)는 선택한 긍정적인 리뷰들을 공백을 구분자로 하여 하나의 긴 문자열로 결합합니다.
예를 들어, 긍정적인 리뷰가 ["Great movie!", "Loved it!", "Highly recommend!"]라면, 결과는 "Great movie! Loved it! Highly recommend!"와 같이 됩니다.


###  순환돌리기 예시
```python
result = []
for token in word_tokens: 
    if token not in stop_words: 
        result.append(token) 
```

### 비트 연산자 (Bitwise Operators)

AND (&): 두 비트가 모두 1일 때 1, 그렇지 않으면 0.

OR (|): 두 비트 중 하나라도 1이면 1, 둘 다 0일 때만 0.

XOR (^): 두 비트가 다를 때 1, 같을 때 0.

NOT (~): 비트를 반전시킴. 0은 1로, 1은 0으로.

왼쪽 쉬프트 (<<): 비트를 왼쪽으로 이동. (곱하기 2)

오른쪽 쉬프트 (>>): 비트를 오른쪽으로 이동. (나누기 2)

### 이터레이터 (Iterator)

__iter__(): 이터레이터 객체 자체를 반환합니다. 이 메서드를 호출하면 이터레이터가 반환됩니다.
__next__(): 이터레이터의 다음 값을 반환합니다. 더 이상 반환할 값이 없으면 StopIteration 예외를 발생시켜야 합니다.

```python
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
# print(next(my_iterator))  # StopIteration 예외 발생
```