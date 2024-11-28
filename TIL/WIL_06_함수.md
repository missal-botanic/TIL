함수 입력은 **매개변수** 모든 타입을 취할 수 있고 모든 타입을 반환 가능하다.

-정의하기(define) : 0개 또는 1개 이상의 매개변수를 갖는다.
-호출하기(call) : 0개 또는 1개 이상의 결과를 얻는다.

#### 매개변수가 없는 함수

```py
def PassThrough():
    pass # 패스문 

PassThrough() # 함수 호출
>>> None
```

```py
def MakeSound():
    print('quack') # 리턴 없이 출력만 있는 함수

MakeSound()
>>> quack
```

```py
def agree(): 
    return True # 리턴 함수
>>> True

if agree(): # if while 문에 함수 붙여서 사용
    print("let's do this")
else:
    print("no")
>>> let's do this
```

```
함수로 전달하는 값은 **인수** 인수의 값이 함수 내에서 **매개변수**에 복사

print(do_noting())
>>> None # 함수에 return 이 없을시 None 출력 (pass 역시 None출력)
# None은 False와 다른 의미이다.
```

```py
def echo(anything): # 인수 -> 매개변수
    return anything + ' ' + anything

echo('Rumplestiltskin')
>>> 'Rumplestiltskin Rumplestiltskin'
```


```py
def commentary(color): # 함수 내 if 문
    if color == 'red':
        return "It's tomatos"
    if color == 'green':
        return "It's green pepper"
    if color == 'bee purple':
        return "I don't know what it is"
    else:
        return "let me know the color " + color + "."

comment = commentary('blue')

print(comment)

>>> let me know the color blue.

print(commentary('red'))
>>> It's tomatos
```

```py
thing = None # None 확인
if thing:
    print("It's some thing")
else:
    print("It's no thing")
>>> It's no thing

thing = None
if thing is None: # is Nones 조건
    print("It's noting")
else:
    print("It's something")
>>> It's noting
```


```
is: 객체가 동일한지 비교. (is not)
==: 값이 같은지 비교.
!=: 값이 다른지 비교.
비교 연산자 (<, >, <=, >=): 크기 비교.
in: 값이 시퀀스에 포함되어 있는지 확인.
not in: 값이 시퀀스에 포함되지 않았는지 확인.
and, or, not: 논리 연산자를 사용하여 복합 조건을 작성.
```
```
None
False
0 (정수 0, 실수 0.0 등)
빈 시퀀스 또는 컬렉션 (예: [], '', {}, () 등)
빈 딕셔너리 {}
빈 집합 set()

빈 자료구조는 False로 나오지만 None과는 같지 않다. 즉 None True False 형이 존재한다.

[''] or ('') 는 True 모든 자료형 동일
```


```py
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None)
>>> None is None
```

