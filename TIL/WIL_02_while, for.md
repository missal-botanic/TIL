
### while

```py
count = 1
while count <=5:
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

```py
for letter in word: # for문은 in을 항상 포함한다.
    print(letter)
```

```py
numbers = [1,3,5]
position = 0
while position < len(numbers):
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
word = [1,3,5]
for letter in word:
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
else: # 중단 되지 않고 모든 항목이 순환되었는지 확인 + 찾지 못함
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
zip()
```

```
a = [range(0,11,2)]
>>> [range(0, 11, 2)]

a = list(range(0, 11, 2))
>>> [0, 2, 4, 6, 8, 10]

a = [list(range(0, 11, 2))]
>>> [[0, 2, 4, 6, 8, 10]]
```
```py
numbers = [3, 2, 1, 0]
for number in numbers:
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
    print("too low")
    number += 1
if number == guess_me:
    print("found it")
else:
    print("oops")
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
guess_me = 7
number = 1
while True: 
    if number < guess_me:
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
guess_me = 7
for number in range(10):
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("Fit it!")
        break
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

guess_me = 7
for number in range(10):
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("Fit it!")
        break
    else: # else는 뒤에 올 수 없음
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
    elif number == guess_me:
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