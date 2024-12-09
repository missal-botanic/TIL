
슬라이싱 원본
```py
print(s[0:len(s):1])
# print(s[::-1])
print(s[len(s)-1::-1]) # 마지막은 미포함이라 -1 필요
```

슬라이싱
```py
s = "abcdefghij"

print(s[0])
print(s[0:1]) # 마지막은 포함 안되기 때문에 결과가 같다.
a
a
```
슬라이싱 역순
```py
words[len(words)-1] # =< > 이기 떄문에 =< >-1 이다.

my_list = [0, 1, 2, 3, 4, 5]
print(my_list[5:1:-1]) # end 부분 -1이다.
>>> [5, 4, 3, 2]
```
슬라이싱 역의 역순
```py
s = 1234567890
s[-7:-3]
>>> 4567
```
짝수, 홀수
```py
s[::2] #홀수
s[1::2] #짝수
```
문자열 교체
```py
s = "I love apples"

result = s.replace("apples", "bananas") # 문자열 교체
print(result)
>>> 'I love bananas'
```
문자열 찾기
```py
s = "Find the index of the first 'e' character"
s.find('e') # index() 없을 시 오류 find()는 -1
try:
    print(index('fja')) # 오류시 우회
except:
    print('error')

# list는 find 없음
# count 는 둘 다 있음
```
공백제거 + 대문자화
```py
s = " OpenAI "
s.strip().upper() #strip은 양쪽 공백제거가 기본 값
#리스트일 경우 바로
s.strip()[1].upper() # 공백 제외 2번째  선택
s[1].strip().upper() # 공백 포함 2번째
```
이메일 자르기
```py
# 01
email = input('이메일 주소를 입력하세요: ')
email = email.strip().split('@')
email_id = email[0]
email_domain = email[-1]
# 02
email_id, email_domain = email.strip().split('@') # 객체가 같으면 '언패킹' 된다.

print(email_id)
print(email_domain)
```
컨프리헨서
```py
words = "dfskofg"
# 01
result = []
for a in range(len(words)):
    if a % 2 == 0:
        result.append(words[a])
print(result)
>>> ['d', 's', 'o', 'g']

# 02
result = [words[a] for a in range(len(s)) if a % 2 == 0]
print(result)
>>> ['d', 's', 'o', 'g']
```
```py
.join # 리스트에 해당
```
.append
```py
fruits = ['apple', 'banana', 'cherry']
fruits.append(['data','blueberry']) # 리스트 통으로 들어감
print(fruits)
>>>
['apple', 'banana', 'cherry', ['data', 'blueberry']]
```
.extend
```py
fruits = ['apple', 'banana', 'cherry', 'watermelon', 'date']
fruits.extend(['melon', 'blueberry']) # 자동 언팩
print(fruits)
>>>
['apple', 'banana', 'cherry', 'watermelon', 'date', 'melon', 'blueberry']
```
[list] + [list]
```py
fruits = ['apple', 'banana', 'cherry', 'watermelon', 'date']
new_fruits = ['melon', 'blueberry']

print(fruits + new_fruits)
>>> ['apple', 'banana', 'cherry', 'watermelon', 'date', 'melon', 'blueberry']
```
'*' 연산 우선
```py
list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2 * 2)
>>> [1, 2, 3, 4, 5, 4, 5]
```
순서 정렬, 역순 정렬
```py
numbers.sort()
numbers.reverse() # 반전 문자열은 안됨, 함수도 같은 개념으로 한번만 사용
numbers.sorted() 
sorted(numbers, reverse=True) # 반전
```
map, filter, reduce + 람다
```py
map(fn, numbers)
filter(fn, numbers)

result = reduce(lambda x, y: x + y, numbers)
```
any, all
```py
# any: 하나라도 짝수인 수가 있으면 True
print(any(x % 2 == 0 for x in numbers))  # True

# all: 모두 짝수라면 True
print(all(x % 2 == 0 for x in numbers))  # False
```
isinstance
```py
sum(range(1,101))

isinstance(item, list) # 타입 확인
```
;
```py
print("first");print("second") # ';' 여러 명령어 쓸때
>>>
first
second
```

```py

a, b = map(int, input().split())
# 추가
fruits.insert(2, "watermelon") # .insert 인덱스 + 내용
# 제거
fruits.remove('grape') # .remove 내용으로 삭제
fruits.pop(1) # .pop index로 삭제



marxes = [1, 2, 3]
other = [4, 5]
marxes.append(other) # '리스트의 끝에 하나의 요소를 추가', '리스트일 경우에도 하나의 리스트'
print(marxes)
>>>
[1, 2, 3, [4, 5]]

fruits = ['apple', 'banana', 'cherry']
fruits.extend(['melon', 'blueberry']) # 리스트의 끝에 리스트의 다수의 요소를 하나씩
print(fruits)
>>>
['apple', 'banana', 'cherry', 'melon', 'blueberry']

fruits = [['apple', 'banana', 'cherry', 'watermelon', 'date']]
new_fruits = ['melon', 'blueberry']
fruits.extend(new_fruits) # .extend 리스트 안에 리스트의 경우 1번 언팩한다.
print(fruits)
>>>
[['apple', 'banana', 'cherry', 'watermelon', 'date'], 'melon', 'blueberry']
```
```py
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [9, 9, 9] # 특정 부분을 교체
print(numbers)
>>>
[1, 9, 9, 9, 5]
```

```py
.sort(reverse=True)
sorted(numbers, reverse=True)
```
```py
b = a # 연계됨
b = a.copy # 연계됨

b = a[:] # 연계되지 않음
b = copy.deepcopy(a) # 연계되지 않음
```
```py

numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    num = 0 # 불필요 01
    num = i ** 2 # 불필요 02
    result.append(num)
result 

numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    num = i ** 2 # 불필요 01
    result.append(num)
result 

numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    result.append(i ** 2)
result

squared_numbers = list(map(lambda x: x**2, numbers))

squared_numbers = [x**2 for x in numbers]
```
```py
matrix = [[1, 2], [3, 4], [5, 6]]
result = 0
for row in matrix:
    for element in row: 
        result += element # 는 result = result + element 변수 정의 이전에 호출되기 때문에 사전 정의가 필요하다.
result
>>>
21


matrix = [[1, 2], [3, 4], [5, 6]]
result = 0
for row in matrix:
    result += sum(row) # sum() 리스트를 다루는 함수
result
>>>
21


result = sum([item for row in matrix for item in row]) # 리스트 않에 넣기
result
>>>
21


total_sum = sum(sum(row) for row in matrix) # 속 리스트 sum 후 더블 sum
total_sum
>>>
21
```

```py
matrix = [[1, 2], [3, 4], [5, 6]]
result = 0
for row in matrix:
    result = sum(row) # 누적되지 않음 잘못된 등호

result
>>>
11

matrix = [[1, 2], [3, 4], [5, 6]]
result = 0
for row in matrix:
    result += sum(row)

result
>>>
21
```
```
s[:-1] # 마지막은 포함되지 않음

print(type(tuple()))

my_tuple += (4,)


letters = 'hello'
letters2 = 'world'

letters += letters2

print(letters)

a = (1, 2)
b = (3, 4)
print(a * 2 + b)
'1, 2, 1, 2, 3, 

my_tuple = (1, [2, 3], {'name' : 'jeyeon'})
my_tuple[1][0] = 'a'
my_tuple
>>>
(1, ['a', 3], {'name': 'jeyeon'}) # 튜플안 리스트는 변경 가능


x, y, z = m_tuble # 언패킹

def func():
    return 1, 2, 3
# 함수가 여러 값을 리턴할 때 튜플로 묶어서 나온다
    return [1, 2, 3]
# 명시적으로 해야함
```

```py
my_tuple = [1, 2, 3, 4]

result = '' 
for item in my_tuple:
    result += str(item) + ' '  # 각 항목을 문자열로 변환하고 공백을 추가

# 결과 문자열에서 마지막 공백 제거
result = result.strip()

print(result)


result = ' '.join(map(str, my_tuple))

print(result)
```

```py
my_tuple = [1, 2, 3, 4]

# 01
result = [] 
for item in my_tuple:
    ", ".join(result.append(str(item))) # 작동 하지 않음
print(result)

# 02
result = [] 
for item in my_tuple:
    result.append(str(item))
print(", ".join(result))
```

```py
my_tuple = (1, [2, 3], {'name' : 'jeyeon'})
my_tuple[1][0] = 'a'
my_tuple

my_tuple[2]['full_name'] = my_tuple[2].pop('name')

print(my_tuple)

# my_tuple[2] 는 호출
# my_tuple[2] = 는 해당 부분에 넣기
my_tuple[2]['full_name'] = 1 딕셔너리의 경우 없는것을 만들 수 있다.
```
```py
my_dict = {'name': 'John', 'age': 25}
my_dict.update({'city': 'New York', 'country': 'USA'})
>>>
{'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
```

```
s = "hello"
t = "python"

print(s+"! "+t)
print(f'{s}! {t}')
print("{}! {}".format(s,t))
```