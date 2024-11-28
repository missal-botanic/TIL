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

### 인수

```py
def menu(wine, entree, dessert):
    return{'wine': wine, 'entree':entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake') # 위치 인수 : 순서 대로 입력법
>>>{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}
```
```py
menu(entree='beef', dessert='bagel', wine='bordeaux') # 키워드 인수 : 인수 지정
```
```py
menu('frontenac', dessert='flan', entree='fish') # 혼합사용 위치 인수가 먼저 와야함
```

```py
def menu(wine, entree, dessert='pudding'): # dessert='pudding' 기본값 지정, 함수 정의 때 계산

    return {'wine': wine, 'entree':entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
>>>>{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}
```

```py
def buddy(arg, result=[]): # result=[]: (누적, 공유) 이 매개변수는 기본값으로 빈 리스트 ([])를 사용합니다. 중요한 점은 기본값으로 가변 객체인 리스트가 사용된다는 것입니다. 즉, result는 함수가 호출될 때마다 동일한 리스트를 참조합니다. 이는 함수 호출 간에 상태가 공유되는 원인이 됩니다.
    result.append(arg)
    print(result)

buddy('a')

buddy('a')  
>>> ['a']
buddy('b') 
>>> ['a', 'b']
buddy('c')  
>>> ['a', 'b', 'c']
```

arg라는 인수의 명칭은 "argument"(인수)의 약어로, 주로 함수나 메서드에서 전달되는 값

*args: 가변 위치 인수를 받을 때 사용합니다. 여러 개의 인수를 튜플로 전달받을 수 있습니다.
**kwargs: 가변 키워드 인수를 받을 때 사용합니다. 여러 개의 인수를 딕셔너리 형태로 전달받을 수 있습니다.


def works(arg):
    result = []
    result.append(arg)
    return result

works('a')
works('b')

>>>['b']


def nonbuggy(arg, result=None): # 함수정의에서 변수 지정하면서 공유는 되지 않게
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')

>>>['a']
['b']


shared_result = []  # 리스트는 밖에서 정의
nonbuggy('c', shared_result)  
>>> ['c']
nonbuggy('e', shared_result)
>>>  ['c', 'e']
nonbuggy('f', shared_result) 
>>> ['c', 'e', 'f']

```
def print_args(*args):
    print('Positional tuple:', args)

print_args()
>>> Positional tuple: ()
#  '*' 은 그 뒤에 있는 변수(args)가 가변 개수의 인수를 받는다는 것을 의미 즉 몇개의 인수를 받을지 정해지지 않을시 사용
# 결과물은 듀플로 출력
# *params 라고도 쓴다.
# 함수 호출 정의에서만 사용가능하다
```

```
def print_args(a, b, *args):
    print('a:', a)
    print('b:', b)
    print('Remaining positional arguments:', args)

print_args(1, 2, 3, 4, 5)

>>>a: 1
b: 2
Remaining positional arguments: (3, 4, 5)
```

• 위치 인수를 함수에 전달하면, 함수 내 위치 매개변수와 일치한다.
• 튜플 인수를 함수에 전달하면, 함수 내 튜플 매개변수가 있다.


• 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 인수로 해석할 수 있다.
args = (2,5,7,'x)
print args (args)
>>> ((2, 5, 7,'×'),)

• args라는 튜플 인수를 함수에 전달하여, 위치 매개변수 *args로 분해할 수 있다. 이것은 튜플 매개변수 args 안에 다시 수집된다.
print_args(*args)
>>> (2, 5, 7, 'x')


• 함수 외부에서 *args는 튜플 인수를 쉼표로 구분된 위치 매개변수로 분해한다.
• 함수 내부에서 *args는 모든 위치의 인수를 단일 인수 튜플로 수집한다. *params와 param라는 이름을 사용할 수 있지만, 외부 인수와 내부 인수 모두에 *args를 사용하는 것이 일반적이다.
*args는 함수 외부에서 분해된 값을 함수 내부에 모은다.

