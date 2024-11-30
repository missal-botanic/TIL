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
람다 함수

```py
my_lambda = lambda: "Hello, World!" # 인수가 없는 람다 함수

print(my_lambda())
>>>
'Hello, world!'

sum_lambda = lambda x, y: x + y # 인수가 있는 람다 함수
print(sum_lambda(3,5))
>>>
8
```

map + 람다함수
```py
map(function, iterable)

def f(x):
    return x + 5

numlist = [1, 2, 3, 4, 5]

f(numlist)
>>> 오류

templist = []

for i in numlist:
    templist.append(f(i))

print(templist)
>>>
[6, 7, 8, 9, 10]

print(map(f, numlist))
>>>
<map object at 0x000002080820C310> # 

print(list(map(f, numlist)))
>>>
[6, 7, 8, 9, 10]

```
콜백 함수
```py
# 콜백 함수
def print_message(message):
    print(f"Message: {message}")

# 다른 함수에서 콜백을 사용
def greet(callback):
    callback("Hello, World!")

# greet 함수는 콜백으로 print_message를 호출
greet(print_message)
>>>
Message: Hello, World!


# 콜백 함수: 숫자가 짝수인지 확인
def is_even(x):
    return x % 2 == 0

# filter 함수에서 콜백을 사용하여 짝수만 필터링
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  
>>>
[2, 4, 6] 출력

#  코드가 복잡해지는 문제입니다. 이는 주로 비동기 프로그래밍에서 자주 발생합니다. 이를 해결하기 위해 Promise, async/await 같은 다른 기법들이 도입되었습니다.
```

제너레이터


sum(range(1,101))
# 마지막으로 호출된 항목을 기억하고 다름값 반환
# 이전 호출기억 없음
# 항상 똑같은 상태로 첫 번째 줄 부터 호출

일반 함수와 **제너레이터 함수**는 **상태 관리**와 **값 반환 방식**에서 중요한 차이점이 있습니다. 주어진 설명을 기반으로 두 함수의 차이를 예시와 함께 비교해 보겠습니다.

### 1. **일반 함수**
일반 함수는 **상태를 기억하지 않고, 호출될 때마다 처음부터 끝까지 실행**됩니다. **반환된 값**은 함수의 실행이 끝날 때마다 사라지고, 함수는 다시 호출될 때마다 **초기 상태로 시작**됩니다.

### 2. **제너레이터 함수**
제너레이터 함수는 **`yield`** 키워드를 사용하여 값을 반환하는 함수입니다. 중요한 점은 제너레이터는 **상태를 기억**하고, **`yield`로 값을 반환할 때마다 실행이 일시 중지**되고, **다음 호출에서 이전 상태에서 이어서 실행**됩니다.

---

### 1. **상태를 기억하고 다른 값을 반환 (제너레이터 함수)**

**제너레이터 함수**는 **상태를 기억**합니다. 즉, 이전 호출에서 반환된 값 이후에 실행을 재개하고, 계속해서 값을 반환합니다.

#### 제너레이터 함수 예시

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # 값을 반환하고 실행을 일시 중지
        count += 1

counter = count_up_to(5)

# 제너레이터의 각 값은 yield에서 반환되며, 다음 호출 시 이어서 실행
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
```

#### 설명:
- 제너레이터 `count_up_to`는 `max` 값까지 숫자를 반환합니다. 각 호출 시마다 **`yield`가 값을 반환**하고 함수는 그 상태에서 멈춥니다.
- `next(counter)`를 호출할 때마다 이전 상태에서 이어서 실행되어 새로운 값을 반환합니다.

#### 출력:
```
1
2
3
4
5
```

- 제너레이터 함수는 **이전에 호출한 위치를 기억**하고, **다음 호출 시 계속해서 값을 반환**합니다.

---

### 2. **이전에 호출을 기억하지 않음 (일반 함수)**

**일반 함수**는 **상태를 기억하지 않으며** 매번 함수가 호출될 때마다 처음부터 끝까지 실행됩니다.

#### 일반 함수 예시

```python
def count_up_to(max):
    count = 1
    while count <= max:
        return count  # 함수가 종료되면 반환
        count += 1

# 일반 함수는 매번 호출 시마다 처음부터 실행
print(count_up_to(5))  # 1
print(count_up_to(5))  # 1
print(count_up_to(5))  # 1
```

#### 설명:
- 일반 함수는 호출될 때마다 **처음부터 끝까지 실행**합니다.
- `return`은 **함수를 종료시키므로** 다음 값은 반환되지 않습니다.
- 호출 시마다 함수는 매번 **초기 상태로 돌아가** 다시 실행되며, **첫 번째 값만 반환**됩니다.

#### 출력:
```
1
1
1
```

- `count_up_to(5)`를 매번 호출하면, 함수는 항상 처음부터 실행되고 첫 번째 `count` 값인 `1`만 반환합니다.

---

### 3. **일반 함수와 제너레이터 함수의 차이점**

| 특징                          | **일반 함수**                            | **제너레이터 함수**                          |
|-------------------------------|------------------------------------------|--------------------------------------------|
| **상태 기억**                  | 이전 호출을 기억하지 않음. 항상 처음부터 실행 | `yield`에서 중지한 상태를 기억하고 계속 실행 |
| **값 반환 방식**               | 함수가 종료될 때 한 번만 반환            | `yield`로 값을 반환하고 함수는 중지된 상태에서 이어서 실행 |
| **다음 호출 시 동작**          | 매번 처음부터 실행                       | 마지막 `yield`에서 멈춘 지점부터 실행      |
| **용도**                       | 단순 계산이나 한 번만 반환할 때 적합    | 반복적인 값 생성, 상태를 기억하면서 반복할 때 적합 |

### 4. **결론**
- **일반 함수**는 호출될 때마다 **항상 처음부터 실행**되며 상태를 **기억하지 않습니다**. 주로 **하나의 결과값을 반환**하는 데 사용됩니다.
- **제너레이터 함수**는 `yield`를 사용하여 **반복적인 값을 반환**하며, 호출될 때마다 이전 상태를 **기억하고 계속 실행**됩니다. 주로 **값을 하나씩 반환**하면서 **반복적인 작업**에 유용합니다.

이렇게 **제너레이터 함수는 상태를 기억**하며, 중간에 값을 **일시적으로 반환하고 실행을 중지**할 수 있어 더 복잡한 반복 작업을 효율적으로 처리할 수 있습니다.

```py
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

my_range
>>> 
<function __main__.my_range(first=0, last=10, step=1)>

ranger = my_range(1, 5)
ranger
>>>
<generator object my_range at 0x000002080895BD10>

for x in ranger:
    print(x)
>>>1
2
3
4

for try_again in ranger:
    print(try_again)
>>>
# 아무일 일어나지 않음
# 제너레이터는 값을 기억하지 않는다
```
yield
```py
import time

def return_abc():
    alphabets = []
    for ch in "ABC":
        time.sleep(1)
        alphabets.append(ch)
    return alphabets

return_abc()
>>>
['A', 'B', 'C']


def return_abc():
    for ch in "ABC":
        time.sleep(1)
        return ch
>>>
A #함수가 return ch를 만나면 ch를 반환하고, 함수는 종료되므로 "A"만 반환됩니다. 나머지 "B"와 "C"는 실행되지 않으며, return 이후의 코드는 실행되지 않습니다.

def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch

for ch in yield_abc():
    print(ch)
>>>
A
B
C # 이 함수는 한 번에 하나의 값만 반환하고, 호출자가 값을 요청할 때마다 함수가 그 지점에서 실행을 재개하여 새로운 값을 반환합니다

def func():
    print("출력 A")
    yield 100
    print("출력 B")
    yield 200
    print("출력 C")
    yield 300

generate = func()
next(generate)
>>>
출력 A
100

next(generate)
>>>
출력 B
200

next(generate)
>>>
출력 C
300

next(generate)
>>>
에러

# yield 가 포함되면 제너레이터

# yield가 들어가 있으면 yield_abc() 해도 실행되지 않는다. 일반 함수가 아니다.

# generate = yield_abc() 
# next(generate) or for i in 해야함

#함수내 yield에서 멈춤 다시 호출시 다음 yield 까지 실행

# reversed() 함수도 같은 개념으로 한번만 사용



```
```
yield는 함수를 제너레이터 함수로 만들며, 값을 하나씩 순차적으로 반환합니다. yield가 호출되면 함수의 실행이 잠시 멈추고, 호출한 곳으로 값을 반환한 뒤, 나중에 다시 호출될 때 그 지점부터 실행을 재개합니다.

반면 return은 함수를 즉시 종료시키고 값을 하나만 반환합니다. 함수가 return을 만나면, 나머지 코드는 실행되지 않고 함수가 종료됩니다.
```

제너레이터 컴프리헨션
```py
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
genobj
>>>
<generator object <genexpr> at 0x0000020808B85230>

for thing in genobj:
    print(thing)
>>>
('a', '1')
('b', '2')
```

```
대괄호 [] - 리스트 컴프리헨션
numbers = [x * 2 for x in range(1, 6)]

중괄호 {} - 집합 컴프리헨션 
numbers_set = {x * 2 for x in range(1, 6)}

중괄호 {} - 딕셔너리 컴프리헨션
squared_dict = {x: x ** 2 for x in range(1, 6)}

괄호 () - 제너레이터 컴프리헨션(안보이게 yield문 실행)
numbers_gen = (x * 2 for x in range(1, 6))
```

데코레이터

```py
def my_decorator(func):
    def wrapper():
        print("함수 호출 전")
        func()
        print("함수 호출 후")
    return wrapper

def say_hello():
    print("안녕하세요")

say_hello()
>>>
'안녕하세요'

say_hello = my_decorator(say_hello) # 수동 테코레이터 필요 01
say_hello() #수동 데코레이터 필요 02
>>>
'함수 호출 전'
'안녕하세요'
'함수 호출 후'

def my_decorator(func):
    def wrapper():
        print("함수 호출 전")
        func()
        print("함수 호출 후")
    return wrapper

@my_decorator # 하나 추가로 자동 데코레이터
def say_hello():
    print("안녕하세요")

```



```py
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

def add_ints(a, b):
    return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

>>>
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8


@document_it
def add_ints(a, b):
    return a + b

>>>
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8

@document_it
@square_it # 누적 가능 + 순서를 따진다.
def add_ints(a, b):
    return a + b

>>>
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
64

```
네임스페이스와 스코프
```py
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
>>> inside change_local: wombat 2233498959472

id(animal)
>>> 2233529638960 # 함수내 변수와 전역 변수는 다르다.
```
```py
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print_global()
>>> 'inside print_global: fruitbat'

print('at the top level:', animal)
>>> 'at the top level: fruitbat'


def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()
>>> 에러 # 외부변수를 바꿀수 없다. 호출만 가능

def change_and_print_global():
    #print('inside change_and_print_global:', animal) #global animal이 선언되기 전에, animal 변수를 함수 내에서 참조하려고 합니다.
    global animal
    animal = 'wombat'
    print('after the change:', animal)
```

```py
locals()
globals()

animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())

animal
>>> 'fruitbat'

change_local()
>>> locals: {'animal': 'wombat'} # 로컬 변수 확인

print('globals:', globals())
>>> ....  '_i2':  "print('globals:', globals())" # 다양한 변수 출력
```
 _와 __사용하기
```
function.__namg__ # 함수 이름 출력
funciton.__doc__ # ``` 설명 ``` 함수 설명 출력
#함수는 '__' 시작하거나 끈나는 함수는 예약어다. 가장 사용하지 않는 패턴

```
재귀함수
```py
# 함수가 자기 자신을 호출
# 무한 재귀 방지 가능

import sys

sys.getrecursionlimit()

sys.setrecursionlimit(1500) # get 과 set 이다
```

```py
def dive():
    return dive()

dive()
>>> 에러 RecursionError: maximum recursion depth exceeded
```

```py
lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]] 

def flatten(lol):
    for item in lol:  # 리스트 lol을 순회
        if isinstance(item, list):  # item이 리스트인지 확인
            for subitem in flatten(item):  # flatten을 재귀적으로 호출 
                yield subitem  # 중첩된 리스트에서 나온 원소를 yield
        else:
            yield item  # 리스트가 아닌 경우 바로 원소를 yield

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item) # yield from
        else:
            yield item

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

```
비동기 함수
```py
# 최신 기능 , 어려움
```
예외
```py
# 에러가 발생될 때 '예외' 사용

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except: # 사용자가 만든 예외
    print('Need a position between 0 and', len(short_list)-1, 'but got', position) 
```

```py
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err: # 시스템 클래스 예외
        print('Bad index:', position)
    except Exception as other: # 시스템 클래스 예외
        print('Something else broke:', other)
```
예외 만들기
```py
value = '아'
try:
    if value not in ['가', '나', '다']:
        raise ValueError("가 나 다 중 하나 필요합니다.")
except ValueError:
    print("에러 발생")
```

```py
class UnexpectedRSPValue(Exception): #예외 클래스 만들기
 '''에러 상속'''

value = '아'
try:
    if value not in ['가', '나', '다']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러 발생")
```
