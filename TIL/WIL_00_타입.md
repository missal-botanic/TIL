```
= 는 ==로
예약어 못씀
암시적 = 생략
기본값 = 문자형 - 튜플 '()'
```
뒤함수
```py
del 
gc.collect() # 가비지 컬렉션 삭제

in
is

''.join()
len()
print()
type()
sorted(numbers, reverse=True) 
sys.getrefcount()

re.sub(r'\d', '*', text) #정규식 표현 re. 세트
copy.deeocopy() # copy. 세트
delattr(person, 'name') # 객체 속성 제거

True, False, None 존재
None과 False가 같이 있을 때는 이 둘은 같지 않다.
```
타입별 추가하기
```py
my_tuple = my_tuple + (3,)
my_list.append(3)
my_dic["C"] = 3
my_set.add(3)
```
### 1) 타입

```
인터프리터 = 쥬피터 방식
클래스와 타입은 같은 의미
코드 한줄 80자 이하 추천
숫자보다는 문자열을 많이 다룬다
```

```
00000000 8비트 1바이트

256 경우의 수를 만들수 있고, 숫자의 조합으로 알파벳 만듬.(영문은 가능)

64비트는 8배짜리.-> 16 32 64로 더 큰숫자를 위해 늘어남.
```

```
객체(데이터 덩어리)
1. 타입
2. 값
3. 고유ID
4. 참조횟수 

강타입 언어 = 값은 볼수도 변경 가능하지만 객체의 '타입'은 변경 할 수 없다.

문자열 타입은 변경할 수 없지만 리스트와 튜플은 변경가능하다.

리터럴(Literal)
정수 리터럴, 실수 리터럴, 복소수 리터럴 3가지가 있습니다.
정수 리터럴 : 0b로 시작하면 2진수, 0o로 시작하면 8진수 ,0~9로 시작하면 10진수, 0x로 시작하면 16진수
실수 리터럴 : 소숫점을 포함하거나 e를 포함합니다.
복소수 리터럴 : j로 끝나면 복소수의 허수를 나타냅니다.

숫자시작 안되고 대소문자 구분한다 언더바는 특별취급 (-,! 안됨)

help("keywords") # 예약어 확인
```

```
0x는 십육진수 (Hexadecimal)
0o는 팔진수 (Octal)
0b는 이진수 (Binary)

0b10 >>> 0b를 10진수로 출력
bin()oct()hex()

이진수: int('101', 2)는 10진수 5입니다.
팔진수: int('12', 8)는 10진수 10입니다.
십육진수: int('A', 16)는 10진수 10입니다.
```
바인딩
```py
x = 10
x = 20

# 10는 주소를 잃어버리고 x에 새로운 20이 연결된다.
```

```py
a=7
a=b

# 7에 a,b 둘다 연결된다.
```

```py
x = y = z = 3 # 1개의 값 3개 연결
```

```py
x = 1
x = y

x = 2 # y는 여전히 1이
단지 x가 다른 것을 가르키게 되었을 뿐이다.
불변 객체는 새로운것을 가르키게 되고, 가변 객체는 값을 바꾸게 된다.
```

```py
b = None # 참조횟수 감소

print(sys.getrefcount(a))  # a에 대한 참조 횟수를 출력
```

```py
type() # 타입 확인 함수
print(type(5+2.0)) # print함수 + 타입 확이 함수
```

### 2) 숫자

```py
'=' # 오른쪽 계산뒤에 왼쪽 적용
```

```py
2 * 1.2 >>> 2.4 # 단위 범위가 큰 타입 우선
```

```py
bool(-45) # True
bool(0.0) # False
```

```py
05 # int 경우ㅊ0을 먼저 쓰지 못한다

05.0 or 5. . # float 경우 5.0으로 자동 처리
```


```py
# 나누기 연산
/ # 부동소수점 포함 출력
// # 정수만 출력
/0 # 예외 발생

% # 나머지 얻기
divmod(9,5) # 몫과 나머지 모두 출력 (듀플로 나온다)
```

```py
a = 3

a - 3 # a의 값은 변하지 않는다. 변수 정의가 없음
a = a - 3 # a 의 값이 바뀐다.
a -= 3 # a 의 값이 바뀐다.

a **= 3 # 제곱 계산
```

```py
-5 ** 2 
>>> -25

(-5) ** 2 # 별도 음수처리 ()필요
>>> 25 
```


```py
chr(65) # int 를 문자열 (chracter)
>>> 'A'

ord('A') # 문자열을 int로 (ordinal position)
>>> 65
```

```py
int('-99') 
>>> -99
int('9_9') 
>>> 99 # 자동 정리

int(10.1) 
>>> 10
int('10.1') 
>>> error # 문자열은 에러처리
```

```py
5e0 
>>> 5.0

5e1 
>>> 50.0

5.0e1 
>>> 50.0

5.0 * (10 ** 1) 
>>> 50.0 # 지수표기법
e2 = x 100
e3 = x 1000
e4 = x 10000
```

```py
1_000_000 # 가독성을 위한 선택적 표현법
1.0_0_1
```

```py
다른줄 함수 연결
# 01
print(a);print(b)

# 02
sum = \
1 + 2 + \
3   # \으로 이어서 가능 

# 03
sum = (1
+ 1
+ 2
) #'('도 이어서 가능
```

```py
disaster = True
if disaster : # == True 생략 or is True 생략
    print('Woe!')
else:
    print("Whee!")
```

```py
furry = True
large = True

if furry:
    if large: # furry == True 생략 or is True 생략
        print("It's a yeti")
    else: # 양자택일의 경우 별도 등식 없음
        print("It's a cat")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's human")
```

```py
color = "mauve"

if color == 'red': # == 실제 의미는 = 단지 사용 빈도수에 의해 밀림
    print('Its tomato') # 문자열을은 "" 추천
elif color == 'green':
    print('Its a pepper')
elif color == 'bee purple':
    print('What is this?')
else: # 무조건 필요
    print('no color')
```

```py
5 < x and x <10
(5 < x) and (x > 10)
5<x<10<999 # 비교연산자 규칙
```

```py
null(none)
정수 0, 부동소수점 0.0
빈문자열' ' 
[ ] ( ) { } set() 
>>> #False
```

```py
some_list = [] # 1) 비어있을 경우 False or 2) 내용 지울때 or 3) 초기에 선언용으로 만들 때
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty")
```

```py
# 하드 코딩
vowels = 'aeiou'
letter = 'o'

if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

# 파이써닉
letter in vowels
>>> True

if letter in vowels:
    print("it is a vowel")
```

```py
vowel_dic = {'a':'apple', 'e':'elephant', 'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dic) # 키 값을 기준으로 실행 된다.
```

```py
# 01
tweet_limit = 280
tweet_string = "Blah" * 50 # := 사용하지 않을 시 

diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print('fitting')
else:
    print("over")
    
# 02
tweet_limit = 280

if diff := tweet_limit - len(tweet_string) >= 0: # := 비교 연산 내에 정의 넣기
    print('fitting')
else:
    print("over")
```
불변 객체와 가변 객체의 경우

`float`는 **불변 객체(immutable)**에 속합니다. 따라서, **변수의 값을 변화시킬 때 기존 객체는 변경되지 않고 새로운 객체가 할당됩니다**. 이를 표에 추가하겠습니다.

또한, **None** 타입도 표에 추가할 수 있습니다. `None`은 **불변 객체**로, 그 자체의 값을 변경할 수 없습니다.

다음은 `float`와 `None`을 포함한 업데이트된 표입니다:

---

| **타입**        | **객체**     | **변수의 값 변화 시 동작**                                                    | **예시**                        |
|-----------------|--------------|----------------------------------------------------------------------------|---------------------------------|
| **불변 객체**   | `int`        | 객체를 변경할 수 없으므로 새로운 값이 할당됨. 기존 객체는 변하지 않음.       | `x = 1`, `x = 2`               |
| **불변 객체**   | `str`        | 문자열을 변경할 수 없으므로 새로운 문자열을 할당해야 함. 기존 객체는 변하지 않음. | `x = "hello"`, `x = "world"`   |
| **불변 객체**   | `tuple`      | 튜플의 값을 변경할 수 없으므로 새로운 튜플을 할당해야 함. 기존 객체는 변하지 않음. | `x = (1, 2, 3)`, `x = (4, 5)`  |
| **불변 객체**   | `frozenset`  | 불변 집합도 마찬가지로 변경 불가. 새로운 집합을 할당해야 함.                  | `x = frozenset([1, 2, 3])`, `x = frozenset([4, 5])` |
| **불변 객체**   | `float`      | `float` 값은 변경할 수 없으며, 새로운 값이 할당되어야 함. 기존 객체는 변하지 않음. | `x = 3.14`, `x = 2.71`         |
| **불변 객체**   | `None`       | `None` 객체는 변경 불가. 새 값을 할당해야 함.                                 | `x = None`, `x = 5`            |

---
---

| **타입**        | **객체**     | **변수의 값 변화 시 동작**                                                    | **예시**                        |
|-----------------|--------------|----------------------------------------------------------------------------|---------------------------------|
| **가변 객체**   | `list`       | 리스트의 값은 변경 가능. 객체 자체를 수정하면 다른 변수들에 영향을 미침.       | `x = [1, 2, 3]`, `x[0] = 10`   |
| **가변 객체**   | `dict`       | 딕셔너리의 값이나 항목을 수정할 수 있음. 다른 변수도 영향을 받음.            | `x = {"a": 1}`, `x["a"] = 10`  |
| **가변 객체**   | `set`        | 집합의 항목을 수정할 수 있음. 다른 변수도 영향을 받음.                        | `x = {1, 2, 3}`, `x.add(4)`    |
| **가변 객체**   | `bytearray`  | 바이트 배열도 가변이므로, 값을 변경하면 다른 변수들이 영향을 받음.            | `x = bytearray([1, 2, 3])`, `x[0] = 10` |

---
---




아래는 숫자 타입,입, 텍스트 타입 등 각 데이터 타입을 표로 정리

| **타입**            | **설명**                                                   | **예시**                                      |
|---------------------|------------------------------------------------------------|----------------------------------------------|
| **숫자 타입 (Numeric Types)**  | 정수, 부동소수점, 복소수 등을 포함                     |                                              |
| **int**             | 정수형 (정수 값)                                           | 5, -42, 1000                                 |
| **float**           | 부동소수점형 (실수 값)                                    | 3.14, -2.71, 0.0                             |
| **complex**         | 복소수형 (실수부 + 허수부)                                | 3 + 4j, 1 - 2j                               |
| **시퀀스 타입 (Sequence Types)** | 순서가 있는 데이터의 집합                                |                                              |
| **list**            | 리스트 (변경 가능한 시퀀스)                               | [1, 2, 3], ['apple', 'banana']               |
| **tuple**           | 튜플 (변경 불가능한 시퀀스)                               | (1, 2, 3), ('a', 'b', 'c')                   |
| **range**           | 범위 (정수의 연속)                                        | range(10), range(1, 5)                       |
| **텍스트 타입 (Text Type)**    | 문자열 데이터                                            |                                              |
| **str**             | 문자열 (텍스트 데이터)                                    | 'hello', "world", 'Python 3'                 |
| **집합 타입 (Set Types)**     | 중복되지 않고 순서가 없는 집합                            |                                              |
| **set**             | 집합 (순서 없음, 중복 불가)                               | {1, 2, 3}, {'apple', 'banana'}               |
| **frozenset**       | 불변 집합 (변경 불가능한 집합)                             | frozenset([1, 2, 3])                         |
| **매핑 타입 (Mapping Type)**  | 키-값 쌍을 가진 데이터 구조                               |                                              |
| **dict**            | 딕셔너리 (키-값 쌍)                                       | {'name': 'John', 'age': 30}                  |
| **불리언 타입 (Boolean Type)**  | 참(True) 또는 거짓(False)을 나타내는 값                  |                                              |
| **bool**            | 불리언 (참 또는 거짓)                                      | True, False                                  |
| **바이너리 타입 (Binary Types)** | 바이너리 데이터를 나타내는 타입                            |                                              |
| **bytes**           | 바이트 객체 (불변 시퀀스)                                 | b'hello'                                     |
| **bytearray**       | 바이트 배열 (변경 가능한 시퀀스)                           | bytearray([65, 66, 67])                      |
| **memoryview**      | 메모리 뷰 (바이트 데이터를 효율적으로 다루는 객체)         | memoryview(b'hello')                         |
| **None 타입**       | 값이 없음을 나타내는 타입                                 | None                                         |
| **NoneType**        | None (값이 없음)                                          | None                                         |

```py
a, b = 10, 20

temp = a
a = b
b = temp

a, b = b, a




```