함수
=============
```
함수 입력은 '매개변수'이며, 모든 타입을 취할 수 있고 모든 타입을 반환 가능하다.

- 정의하기(define) : 0개 또는 1개 이상의 매개변수를 갖는다.
- 호출하기(call) : 0개 또는 1개 이상의 결과를 얻는다.
- 함수로 전달하는 값은 '인수' 인수의 값이 함수 내에서 '매개변수'에 복사
```

#### 매개변수가 없는 함수

```py
def PassThrough():
    pass # 패스문, 리턴도 출력도 없는

PassThrough() # 함수 호출
>>> '출력없음'

result = PassThrough()  # 함수 호출
print(result)  # 결과 출력
>>> None # 함수에 return 이 없을시 None 출력

# None은 False와 다른 의미이다.
```

```py
def MakeSound():
    print('quack') # 리턴 없이 출력만 있는 함수

MakeSound()
>>> 'quack'
```

```py
def agree(): 
    return True # 리턴 함수
>>> True

if agree(): # if, while 문에 함수 붙여서 사용
    print("let's do this")
else:
    print("no")

>>> "let's do this"
```

```py
#인수가 매개변수가 된다.

def echo(anything): # 'anything'은 매개변수
    return anything + ' ' + anything

echo('Rumplestiltskin') # "Rumplestiltskin"는 인수
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

print(commentary('red')) # print문 안에 정의
>>> It's tomatos
```

```py
thing = None

if thing: # thing은 True, None은 False 취급
    print("It's some thing")
else:
    print("It's no thing")
>>> "It's no thing"

thing = None
if thing is None: # 'is' Nones 조건
    print("It's noting")
else:
    print("It's something")
>>> "It's noting"
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
# None과 False가 같이 있을 때는 이 둘은 같지 않다.
# None True False 형이 존재한다.
# 빈 자료구조는 False
# [''] or ('') 공백 빈자료가 아니다 True 취급
```

### 인수

```py
def menu(wine, entree, dessert): # 위치 인수
    return{'wine': wine, 'entree':entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake') # 위치 인수 : 순서 대로 대응
>>>{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}

menu(entree='beef', dessert='bagel', wine='bordeaux') # 키워드 인수 : 인수 지정, 순서 변경 가능

menu('frontenac', dessert='flan', entree='fish') # 혼합사용 위치 인수가 먼저 위치함
```

```py
def menu(wine, entree, dessert='pudding'): # dessert='pudding' 기본값 지정, 함수 정의 때 미리 지정됨
    return {'wine': wine, 'entree':entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
>>>>{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}
```

```py
def buddy(arg, result=[]): # result=[]: (누적, 공유) 매개변수는 함수 정의 때 한번 실행된다. 함수라 호출할 때 마다 정의 되는 것이 아니라 리셋 되지 않는다. 이는 함수 호출 간에 상태가 공유된다.
    result.append(arg)
    print(result)

buddy('a')  
>>> ['a']
buddy('b') 
>>> ['a', 'b']
buddy('c')  
>>> ['a', 'b', 'c']
```
```
arg라는 인수의 명칭은 "argument"(인수)의 약어로, 주로 함수나 메서드에서 전달되는 값

*args: 가변 위치 인수를 받을 때 사용합니다. 여러 개의 인수를 튜플로 전달받을 수 있습니다.
**kwargs: 가변 키워드 인수를 받을 때 사용합니다. 여러 개의 인수를 딕셔너리 형태로 전달받을 수 있습니다.
```

```py
def works(arg):
    result = [] # 함수 호출 시 매번 리스트 초기화
    result.append(arg)
    return result

works('a')
works('b')
>>> ['b']


def nonbuggy(arg, result=None): #  None은 불변 객체이므로 매번 함수 호출 시 기본값으로 None이 새롭게 평가됩니다.
    if result is None: 
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')
>>>
['a']
['b']


shared_result = []  # 리스트는 밖에서 정의
nonbuggy('c', shared_result)  
>>> ['c']
nonbuggy('e', shared_result)
>>>  ['c', 'e']
nonbuggy('f', shared_result) 
>>> ['c', 'e', 'f']

# result=[]의 경우 리스트와 같은 mutable object는 한 번 평가되면 그 이후로 계속 같은 객체가 사용됩니다. 이 때문에 함수가 여러 번 호출되어도 항상 같은 리스트 객체를 공유하게 되어 값이 누적됩니다. 반면, result=None은 불변 객체인 None을 기본값으로 설정하는 것입니다. None은 항상 같은 객체이지만, 기본값을 None으로 설정하는 이유는 각각의 함수 호출마다 None이 새로 전달되도록 하기 위해서입니다. 그 후 함수 내부에서 None일 경우에만 새로운 리스트를 생성하므로, 매 호출마다 새로운 리스트가 만들어집니다. 숫자(int), 문자열(str), 튜플(tuple)
```

```py
def print_args(*args): # 정해지지 않은 개수를 받을 때
    print('Positional tuple:', args)

print_args()
>>> Positional tuple: ()
#  '*' 은 그 뒤에 있는 변수(args)가 가변 개수의 인수를 받는다는 것을 의미 즉 몇개의 인수를 받을지 정해지지 않을시 사용
# 결과물은 듀플로 출력
# *params 라고도 쓴다.
# 함수 호출 정의에서만 사용가능하다

def print_args(a, b, *args): # 여러개를 받는 경우 격리되어 받아진다.
    print('a:', a)
    print('b:', b)
    print('Remaining positional arguments:', args)

print_args(1, 2, 3, 4, 5)
>>>
a: 1
b: 2
Remaining positional arguments: (3, 4, 5) # 별도로 모여진다.
```
```py
• 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 인수로 해석할 수 있다.
args = (2,5,7,'x')
print args(args)
>>> ((2, 5, 7,'×'),)

• args라는 튜플 인수를 함수에 전달하여, 위치 매개변수 *args로 분해할 수 있다. 이것은 튜플 매개변수 args 안에 다시 수집된다.
print_args(*args)
>>> (2, 5, 7, 'x')

• 함수 외부에서 *args는 튜플 인수를 쉼표로 구분된 위치 매개변수로 분해한다.
def example(a, b, c):
    print(a, b, c)

# 튜플을 사용하여 함수 호출
args = (1, 2, 3)
example(*args)  # *args는 튜플을 개별 인수로 분해

• 함수 내부에서 *args는 모든 위치의 인수를 단일 인수 튜플로 수집한다. 
1 2
(3, 4, 5)

# *params와 param라는 이름을 사용할 수 있지만, 외부 인수와 내부 인수 모두에 *args를 사용하는 것이 일반적.
# *args는 함수 외부에서 분해된 값을 함수 내부에 결합.
# *args는 항상 맨 마지막에 위치.
```
키워드 인수 분해/모으기 *
```py
def print_kwargs(**kwargs): # 개수가 정해지지 않은 딕셔너리
    print('Keyword arguments:', kwargs)

print_kwargs() # 빈 함수 호출시 빈 값 호출
>>> Keyword arguments: {}

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon') # 호출된 개수 만큼 배분
>>> Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
```
키워드 전용 인수
```py
def print_info(name, age, *, city, country): # name, age 위치 인수 /city, country 키워드 인수

def print_data(data, *, start=0, end=100): #  '*' 이후에 정의된 매개변수들은 모두 위치 인자가 아니라 키워드 인자로만 전달될 수 있
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
>>>
a
b
c
d
e
f

print_data(data, start=4)
>>>
e
f

print_data(data, end=2)
>>>
a
b

print_data(data, data)
>>> 
오류

# *는 Python에서 매개변수 이름 뒤에 사용되며, 이후의 모든 매개변수는 위치 인자가 아니라 키워드 인자로만 받을 수 있음을 나타냅니다. 즉, start와 end는 반드시 명시적으로 이름을 지정해 주어야 합니다. 이 구문은 위치 인자와 키워드 인자를 구분하는 데 사용됩니다
```

가변/불변 인수

```py
outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'terrible'

outside
>>> ['one', 'fine', 'day']

mangle(outside)
outside
>>> ['one', 'terrible', 'day'] 
# 가변 객체(mutable objects)는 함수 내부에서 수정가능.
# 불변 객체 함수 내부에서 객체를 수정하려고 해도 새로운 객체를 생성.
```
독스트링(함수 설명)
```py
def echo(anything):
    'ehco return its input argument' # 짧은 독스트링
    return anything

help(echo.__doc__)
>>> 
''' No Python documentation found for 'ehco return its input argument'. 
Use help() to get the interactive help utility. 
Use help(str) for help on the str class. '''


def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* 
    ''' # 긴 독스트링
    if check:
        print(thing)

help(print_if_true)
>>>
'''Help on function print_if_true in module __main__:
print_if_true(thing, check)
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first*'''
```
