
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
sep="", end="" 
```py
print('naver','kakao','sk','samsung', sep=";")
print("first", end=""); print("second") # end="" 자동 줄바꿈 제거
>>>
firstsecond
```