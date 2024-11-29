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
```
arg라는 인수의 명칭은 "argument"(인수)의 약어로, 주로 함수나 메서드에서 전달되는 값

*args: 가변 위치 인수를 받을 때 사용합니다. 여러 개의 인수를 튜플로 전달받을 수 있습니다.
**kwargs: 가변 키워드 인수를 받을 때 사용합니다. 여러 개의 인수를 딕셔너리 형태로 전달받을 수 있습니다.
```

```py
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

```py
def print_args(*args):
    print('Positional tuple:', args)

print_args()
>>> Positional tuple: ()
#  '*' 은 그 뒤에 있는 변수(args)가 가변 개수의 인수를 받는다는 것을 의미 즉 몇개의 인수를 받을지 정해지지 않을시 사용
# 결과물은 듀플로 출력
# *params 라고도 쓴다.
# 함수 호출 정의에서만 사용가능하다

def print_args(a, b, *args):
    print('a:', a)
    print('b:', b)
    print('Remaining positional arguments:', args)

print_args(1, 2, 3, 4, 5)

>>>a: 1
b: 2
Remaining positional arguments: (3, 4, 5)

• 위치 인수를 함수에 전달하면, 함수 내 위치 매개변수와 일치한다.
• 튜플 인수를 함수에 전달하면, 함수 내 튜플 매개변수가 있다.

• 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 인수로 해석할 수 있다.
args = (2,5,7,'x')
print args (args)
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
(3, 4, 5) # 단일 인수 튜플
*params와 param라는 이름을 사용할 수 있지만, 외부 인수와 내부 인수 모두에 *args를 사용하는 것이 일반적이다.
*args는 함수 외부에서 분해된 값을 함수 내부에 모은다.
*args는 항상 맨 마지막에 위치해야 합니다.
```

```py
def print_kwargs(**kwargs): #
    print('Keyword arguments: ', kwargs)

print_kwargs()
>>> Keyword arguments:  {}

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
>>> Keyword arguments:  {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
```

```py
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)

```


키워드 인수 분해/모으기 *

```py
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data) # 1개 리스트 단일 데이터 인풋
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
>>> 오류
#*는 Python에서 매개변수 이름 뒤에 사용되며, 이후의 모든 매개변수는 위치 인자가 아니라 키워드 인자로만 받을 수 있음을 나타냅니다. 즉, start와 end는 반드시 명시적으로 이름을 지정해 주어야 합니다. 이 구문은 위치 인자와 키워드 인자를 구분하는 데 사용됩니다
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
>>> ['one', 'terrible', 'day'] #  가변 객체(mutable objects)는 함수 내부에서 수정될 수 있다
#불변 객체는 함수에 전달할 때 객체의 복사본이 전달되는 것처럼 보이며, 함수 내부에서 객체를 수정하려고 해도 새로운 객체를 생성하는 효과가 있습니다
```

독스트링
```py
def echo(anything):
    'ehco return its input argument' # 짧은 독스트링
    return anything

help(echo.__doc__)
>>> No Python documentation found for 'ehco return its input argument'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


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
>>> Help on function print_if_true in module __main__:

print_if_true(thing, check)
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first*
```

```
모든 것은 객체다.
객체 : 숫자, 문자열, 튜플, 리스트, 딕셔너리
일등시민 : 함수
함수를 변수에 할당, 다른 핫무에서 이를 인수로 사용, 함수에서 이를 반환
```

```py
def answer():
    print(42)

def run_something(func):
    func()

run_something(answer)
>>> 42
```

```
()가 없으면 객체로 전달된다. answer는 객체로 전달 된 것이다.
type(run_something)
>>> function
```

```py
def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)
>>> 14
```

```py
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)

>>> 10
```
내부함수

```py
def outer(a, b):
    def inner(c, d): # 1차 정의 2차 호출
        return c + d
    return inner(a, b) # a->c, b->d

outer(4,7)
>>> 11


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '{}'".format(quote)
    return inner(saying)

knights('Ni!')
>>> "We are the knights who say: 'Ni!'"
```

크로저
```py
def knight2(saying):
    def inner2():
        return "We are the knights who say: %s" % saying
    return inner2 # 내부 함수를 반환하겠다.(실행x + saying 값도 기억)

a = knight2('Duck')
b = knight2('Hapsenpfeffer')

type(a)
>>> function
type(b)
>>> function

a
>>> <function __main__.knight2.<locals>.inner2()>
b
>>> <function __main__.knight2.<locals>.inner2()>

a()
>>> 'We are the knights who say: Duck'
b()
>>> 'We are the knights who say: Hapsenpfeffer'
```

```py
def outer():
    x = 10
    def inner():
        return x  # x는 outer 함수 내의 지역 변수
    return inner # 내부 함수를 변수로 지정하겠다는 의미(함수 실행이 아니라 함수 전달 + outer 입력값 x = 10 도 같이 기억)

f = outer()
print(f())  # 출력: 10

# 외부 함수는 사라지지만 외부함수의 인수 값은 기억하고 있다.
# 두번째 호출되면 내부 클로저 함수만 실행되고 이전에 기억한 함수가 쓰인다.
```


