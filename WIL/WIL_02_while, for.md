
### while

```py
# while문

count = 1
while count <=5: # while 뒤에는 항상 조건 필요
    print(count)
    count += 1
>>>
1
2
3
4
5
```

```py
# while + True + break

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
>>>
String to capitalize [type q to quit]:  google
Google
String to capitalize [type q to quit]:  q
```

```py
# while + continue 

while True:
    value = input("Integer ,please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue # 아래꺼 실행하지 말고 다시 돌아가
    print(number, "squared is", number * number)
>>>
Integer ,please [q to quit]:  3
3 squared is 9
Integer ,please [q to quit]:  2
```

```py
# for문 긴버전

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
>>>
t
h
u
d
```

### for
파이서닉
```py
for letter in word: # for문은 in을 항상 포함한다.
    print(letter) # for, if 다음 명령어는 들여쓰기
```

```py
# while <-> for
numbers = [1,3,5]
position = 0
while position < len(numbers): # 개념적 접근
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', numbers)
        break
    position += 1
else:
    print('No even number found')
>>>
No even number found
```

```py
# for <-> while
word = [1,3,5]
for letter in word: # 파이써닉 방법
    if letter % 2 == 0:
        print("Found even number", letter)
        break
else:
    print("No even number found")
>>>
No even number found
```

```py
word = 'thud'
for letter in word:
    if letter == 'u':
        break # 아래까지 진행하지 않음
    print(letter)
>>>
t
h
```

```py
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else: # for에 대한 else. 중단 되지 않고 모든 항목이 순환되었는지 확인 + 찾지 못함
    print("No 'x' in there.")
>>>
t
h
u
d
No 'x' in there.
```

```py
range(start = 0, stop = 꼭 입력, step = 1) # default
range(3) = range(0, 3) = range(0, 3, 1)
list(range(0,11,2))
```

```py
a = [range(0,11,2)] # 자료 형태를 정해주어야 한다.
print(a)
>>> [range(0, 11, 2)]

a = list(range(0, 11, 2)) # 일반적인 모습
print(a)
>>> [0, 2, 4, 6, 8, 10]

a = [list(range(0, 11, 2))] # 이중 구조화
>>> [[0, 2, 4, 6, 8, 10]]
```
```py
numbers = [3, 2, 1, 0]
for number in numbers: # 앞 number(단수), 뒤 numbers(복수)는 다르다. 
    print(number)
>>>
3
2
1
0
```

```py

guess_me = 7
number = 1
while number < guess_me:
    print(number, "too low")
    number += 1
    if number == guess_me: # if문 루프 안에 위치
        print("found it")
    else: # 반복 실행
        print("oops")
>>>

1 too low
oops
2 too low
oops
3 too low
oops
4 too low
oops
5 too low
oops
6 too low
found it

guess_me = 7
number = 1
while number < guess_me:
    print(number, "too low")
    number += 1
if number == guess_me: # if문 루프 밖에 위치
    print("found it")
else:
    print("oops") # while 모두 실행 이후 넘어옴
>>>
1 too low
2 too low
3 too low
4 too low
5 too low
6 too low
found it

```

```py
guess_me = 7
number = 1
while True: # True 상태에는 무한 반복
    if number < guess_me: # if문 푸르 안에 위치
        print("too low")
    elif number == guess_me:
        print("found it")
        break # 필요
    else:
        print("oops")
    number += 1 #필요
>>>
too low
too low
too low
too low
too low
too low
found it
```

```py
# 01
 
guess_me = 7
for number in range(10):
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("Fit it!")
        break
    elif number > guess_me: # elif로 마무리
        print("too much")
        break
>>>
too low
too low
too low
too low
too low
too low
too low
Fit it!

# 02

guess_me = 7
for number in range(10):
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("Fit it!")
        break
    else: # else로 마무리
        print("too much")
>>>
too low
too low
too low
too low
too low
too low
too low
Fit it!

guess_me = 7
number = 1
for number in range(10):
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me: # break문 없음
        print("Fit it!")
    elif number > guess_me:
        print("too much")
        break
>>>
too low
too low
too low
too low
too low
too low
too low
Fit it!
too much
```
```py
# if 문 연산자

is: 객체가 동일한지 비교. (is not)
==: 값이 같은지 비교.
!=: 값이 다른지 비교.
비교 연산자 (<, >, <=, >=): 크기 비교.
in: 값이 시퀀스에 포함되어 있는지 확인.
not in: 값이 시퀀스에 포함되지 않았는지 확인.
and, or, not: 논리 연산자를 사용하여 복합 조건을 작성.
```