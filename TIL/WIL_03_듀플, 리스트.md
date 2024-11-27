자료구조
============

```
중복된값 사용 = 리스트
고유값만 사용 = 셋
```

### 튜플

```py
empty_tuple = ()
```

```py
one_marx = "Groucho", # ','생략하면 문자열, 함수에 인자로 넣으면 문자열로 인식 괄호 꼭 필요
marx_tuple =  "Groucho", "Chico", "Harpo"

one_marx = ("Groucho",) # ','생략하면 문자열 one_marx = ("Groucho") 다름
marx_tuple =  ("Groucho", "Chico", "Harpo")
```

```py
marx_tuple =  ("Groucho", "Chico", "Harpo")
a,b,c = marx_tuple # 1:1 각각 할당
print(a)
>>>'Groucho'
```

```py
a = 1
b = 2

a, b = b, a # 각각 할당 2

print(a)
>>> 2
print(b)
>>> 1
```


```py
marx_list = [1, 2, 3]
tuple(marx_list)
print(marx_list)
>>> (1, 2, 3) # 리스트 -> 튜플
```

```py
marxes[0] >>> 듀플의 특정 값을 추출
```

```py
(1,) + (2,3) 
>>> (1, 2, 3) # 튜플 합치기

('1',) * 3
>>> ('1','1','1') # 튜플 연산

t1 = (2, 3, 4)
t2 = (1,)
t1 += t2
>>> (2, 3, 4, 1) # 새로운 변수가 만들어 지는 것이다.
```




### 리스트

```py
list() # 리스트함수 생성

#split() >>> 결과물이 리스트로 나옴
```

```py
list('cat') # 리스트 기본 함수
>>> ['c', 'a', 't']
list('한')
>>> ['한']
```

```py
a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)
>>>['ready', 'fire', 'aim'] # 튜플을 리스트화
```

```py
b = a.copy() # 새로운 카피본 단 리스트는 여전히 연결되어 있다.
c = list(a)
d = a[:]
```

```py
b = copy.deepcopy(a) # 변수 안에 속한 리스트 모두 개별 카피
```

```py
.append() # 끝에 항목 추가
marxes.append('4')
>>> [1, 2, 3, 4]

other = [4, 5]
marxes.append(other)
>>> [1, 2, 3,[4, 5]]
```

```py
.insert
marxes.insert(2, 'Gummo') # 2번 인덱스에 추가

.extend()
marxes.extend(others) #리스트 병합
```

```py
marxes += others #리스트 끼리 더하기
```

```py
["a"] * 3 # 리스트 연산
>>> ['a', 'a', 'a']
```

```py
marxes = ['a', 'b', 'c']
separator = '*'
joined = separator.join(marxes) # joined.split(seperator) joind은 문자열 메서드 이다.
joined
>>>
'a*b*c'
```

```py
del numbers[-1] # 마지막 값 삭제 # '=' 의 반대 값 으로 함수나 메서드가아니라 '구분'이다.
```

```py
.remove()
marxes.remove('a') #이름으로 삭제

.pop() = .pop(-1) # 항목 삭제 + 삭제한 항목 출력

.append() -> .pop() >>> 후입 선출 스택(stack)
.append() -> .pop(0) >>> 선입 선출 큐(queue)

.clear() # 모든 항목 삭제
```

```py
numbers = [1, 2, 3, 4]
numbers[1:3] = [] # 해당 부분을 빈 리스트로 전환
numbers
>>>
```

```py
marxes[2], marxes[1:3]

marxes = marxes[::-1] # 원본에는 변함 없음 (원본은 주소를 잃음)

.reverse() # 원본이 변함
marxes.reverse()
```


```py
.index('a') >>> 1 # 값으로 오프셋 찾기, 값이 2개 이상이면 처음 값만 반환

.count('a') >>> 2 # 몇개의 특정 항목이 있는지 카운트
```

```py
'a' in marxes >>> True # 존재 여부 확인

```

```py
marxes.sort() # 원본
marxes.sort(reverse = True) # 원본 역순

sorted_marxes = sorted(marxes) # 복사본

len()
```

```py
a = [3, 2]
b = [1, 2, 3]
a>b
>>>
True #순차적 비교 만약에 0번에서 결정나면 이후 비교는 하지 않는다. 지속해서 같은 경우
``` 

```py
for 리스트 zip(리스트) # 가작 작은 리스트 기준으로 조합
```

```py
a = '1', '2', '3'
b = 'A', 'B', 'C'

list(zip(a, b))
dict(zip(a, b))
>>> [('1', 'A'), ('2', 'B'), ('3', 'C')]
```

```py
number_list[]
number_list.append(1)
number_list.append(2)
```

```py
number_list = list(range(1,6))
```

```py
number_list[]
for number in range(1,6):
    number_list.append(number)
```

```py
number_list = [number for number in range(1,6)] #for 문 한줄 연결 샘플

numbers = []  # 긴버전
for number in range(1, 6): 
    numbers.append(number)  

```

```py
number_list = [number for number in range(1,6) if number % 2 == 1]
```

```py
number_list[]
for number in range(1,6):
    if number % 2 == 1:
        number_list.append(number)
```

```py
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)
>>>
1 1
1 2
2 1
2 2
3 1
3 2
```

```py
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
for now, col in cells:
    print(row, col)
>>>
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
3 1
3 2
3 1
3 2
3 1
3 2
```

```py
all_birds[1][0] # 다중 리스트일 때 선택하는 방법
```

```py
things[1].capitalize() # 할당전
things[1] = things[1].capitalize() # 실제 할당
```

```py
things[-1] = things[-1].lower()
things[-1] = things[-1][::-1]
things[-1].capitalize()
```

```py
things[-1] = things[-1].lower()[::-1].capitalize() #최소화
```

듀플이 적은공간 차지

```py
even = range(10) # 객체 저장
>>>range(0, 10)
even = [range(10)] # 객체 저장
>>>[range(0, 10)]
even = list(range(10)) #리스트 저장
>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```py
numbers = list(range(10))
even = [] # 정의 꼭 필요 없으면 재실행 시 누적됨 초기화 역할을 함
for number in numbers:
    if number % 2 == 0:
        even.append(number)
even

for number in range(10): # 좀더 간소화 버전
```


```py
start1 = 'a','b','c'
start1_caps = " ".join([word.capitalize() + "!" for word in start1])
start1_caps


for word in start1:
    capitalized_word = word.capitalize() + "!"
```


