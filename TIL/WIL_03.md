empty_tuple = ()

one_marx = "Groucho", # ,생략하면 문자열, 함수에 인자로 넣으면 문자열로 인식 괄호 꼭 필요
marx_tuple =  "Groucho", "Chico", "Harpo"

one_marx = ("Groucho",) #,생략하면 문자열
marx_tuple =  ("Groucho", "Chico", "Harpo")

marx_tuple =  ("Groucho", "Chico", "Harpo")
a,b,c = marx_tuple
print(a)
>>>'Groucho'


```py
a = 1
b = 2

a, b = b, a

print(a)
>>> 2
print(b)
>>> 1
```

marx_list = [1, 2, 3]
tuple(marx_list)
print(marx_list)
>>> (1, 2, 3)

(1,) + (2,3)
>>> (1, 2, 3)

('1',) * 3
>>> ('1','1','1')

t1 = (2, 3, 4)
t2 = (1,)
t1 += t2
>>> (2, 3, 4, 1) # 새로운       t1이 만들어 지는 것이다.

중복된값 사용 = 리스트
고유값만 사용 = 셋

marxes[0] >>> 리스트의 특정 값을 추출
split() >>> 결과물이 리스트로 나옴

list() # 리스트함수 생성
list('cat')
>>> ['c', 'a', 't']
list('한')
>>> ['한']

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)
>>>['ready', 'fire', 'aim']


marxes = marxes[::-1] # 원본에는 변함 없음 (원본은 주소를 잃음)

.reverse() # 원본이 변함
marxes.reverse()

.append() # 끝에 항목 추가
marxes.append('4')

.insert
marxes.insert(2, 'Gummo') # 2번 인덱스에 추가

["a"] * 
>>> ['a', 'a', 'a']