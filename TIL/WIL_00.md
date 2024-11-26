```
= 는 ==로
예약어 못씀
암시적 = 생략
기본값 = 문자형 - 튜플


del 
in
len()
join()
sorted() reverse()
copy.deeocopy()
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
객체(데이터 덩어리) = 타입, 값, 고유ID, 참조횟수 

강타입 언어 = 값은 볼수도  변경 가능하지만 객체의 '타입'은 변경 할 수 없다.

문자열 타입은 변경할 수 없지만 리스트와 튜플은 변경가능하다.

리터럴 , 변수

숫자시작 안되고 대소문자 구분한다 언더바는 특별취급 (-,! 안됨)

help("keywords") # 예약어 확인
```

```
x = 10
x = 20

10는 주소를 잃어버리고 x에 새로운 20이 연결된다.
```

```
a=7
a=b

7에 a,b 둘다 연결된다.
```

```
x = y = z = 3 # 가능
```

```
x = 1
x = y

x = 2 # y는 여전히 1이다. 단지 x가 다른 것을 가르키게 되었을 뿐이다.
불변 객체는 새로운것을 가르키게 되고, 가변 객체는 값을 바꾸게 된다.
```

```
type()
print(type(5+2.0))
```

```
b = None # 참조횟수 감소
print(sys.getrefcount(a))  # a에 대한 참조 횟수를 출력
```

### 2) 숫자

```
= 오른쪽 계산뒤에 왼쪽 적용
2 * 1.2 >>> 2.4 # floats 가 우선
```

```
bool(-45) # true
bool(0.0) # false
```

```
05 는 쓰지 못한다.
05.0 or 5. 는 5.0 이다
```


```py
/ 부동소수점 포함 출력
// 정수만 출력
/0 예외 발생
% 나머지 얻기
divmod(9,5) 몫과 나머지 출력 (듀플로 나온다)
```

```py
a = 3

a - 3 # a의 값은 변하지 않는다.
a = a - 3 # a 의 값이 바뀐다.
a -= 3 # a 의 값이 바뀐다.

a **= 3 # 제곱 계산
```

```py
-5 ** 2 >>> -25
(-5) ** 2 >>> 25
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

```py
chr(65) >>> 'A'
ord('A') >>> 65
```

```py
int('-99') >>> -99
int('9_9') >>> 99

int(10.1) >>> 10
int('10.1') >>> error
```

```py
5e0 >>> 5.0
5e1 >>> 50.0
5.0e1 >>> 50.0
5.0 * (10 ** 1) >>> 50.0
```

```py
1_000_000 으로 표현 하기도 함
1.0_0_1
```



```py
sum = \
1 + 2 + \
3   # \으로 이어서 가능 
```

```py
sum = (1
+ 1
+ 2
) #'('도 이어서 가능
```

```py
disaster = True
if disaster :
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
    else: # 양자택일의 경우
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
5<x<10<999
```


null(none), 정수 0, 부동소수점 0.0, 빈문자열' ' [ ] ( ) { } set() = **False**


```py
some_list = [] # 비어있을 경우 False
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty")
```

```py
letter = 'o' # 하드 코딩
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
```

```py 
vowels = 'aeiou'
letter = 'o'
letter in vowels

if letter in vowels:
    print("it is a vowel")
```

```py
vowel_dic = {'a':'apple', 'e':'elephant', 'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dic) # 키 값을 기준으로 한다.
```

```py
tweet_limit = 280
tweet_string = "Blah" * 50 # := 사용하지 않을 시 
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print('fitting')
else:
    print("over")
```

```py
tweet_limit = 280
tweet_string = "Blah" 
if diff := tweet_limit - len(tweet_string) >= 0: # := 비교 연산 내에 정의 넣기
    print('fitting')
else:
    print("over")
```