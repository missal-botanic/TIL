## 1. 한줄코드

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
  
### 3)텍스트 문자열

시퀀스 시스템
문자열은 불변

print() 출력은 인터프리터와 아이들과 출력방식이 다르다
아이들은 따움표가 생략되고 줄 바꿈은 \n 로 표시 된다.

\n 줄바꿈 
\t 띄어 쓰기 
"\"hi\""
\\ 는 실제 \ 표시

r"" 원시 문자열\n 은 내용 그대로 전부 출력 하지만 print() 구문은 이스케이프 적용되어 출력

"hello"+"baby" >>> 'hellobaby'
"hello""baby" >>> 'hellobaby'
('a' + "e" + '''i''' + """u""") >>> 'aeiu'
print('a' + "e" + '''i''' + """u""") >>> 'aeiu'

a = 'a'
b = "e"
c = '''i'''
d = """u"""
print(a + b + c + d) >>> 'aeiu'

start = 'Na' * 4 + '\n'
middle = 'hey' * 3 + '\n'
end = 'Goodbye'
print(start + start + middle + end)
>>>NaNaNaNa
NaNaNaNa
heyheyhey
Goodbye # 줄바꿈보다 *이 더 높은 우선순위

letter[0] # 첫문자 선택

letter[0] = 'p' >>> # 오류 발생

letter.replace('H', 'P') # 함수 방식
'P' + letter[1:] # 슬라이스 방식

슬라이스

시작, 끝, 스텝

[:] 전체 [s:] s부터 끝까지 [:e] 시작부터 e-1 까지 [s:e:st] st만큼 건너 뛰면서

letters[-3:0] >>> 'xyz'
letters[-6:-2] >>> 'uvwx'
letters[::7] >>> 'ahov'
letters[::-1] = letters[-1::-1] >>> zyx...cba
letters[70:71] >>> ''

len(letters)

string.function(arguments) 메서드 기본 구조 ()안에서는 인수가 들어간다. 인수가 없을 시에도 ()는 들어간다.

.split()

letters = "abc, def, hij"
letters.split(",") >>> ['abc', 'def', 'hij']

.join()

letters = ['abc', 'def', 'hij']
new_letters = ','.join(letters) 
>>>'abc,def,hij'

.replace()

letters.replace('a', 'b') a를 b로 바꾼다.
letters.replace('a', 'b', 100) 100회 까지 바꾼다.

.strip() # 맨 앞 or 맨 뒤 ' ', \n , \t 자동 제거
.lstrip() # 왼쪽(시작)만 제거
.rstrip() # 오른쪽(끝)만 제거

letter('!') # !가 없으면 아무 일도 일어나지 않는다.

"hello....!!!?" .strip('.!?') >>> "hello"

```py
import string

string.whitespace >>> ' \t\n\r\x0b\x0c'
string.punctuation >>> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

letters.strip(string.whitespace + string.punctuation)# 앞선 호출은 확인용
```

len(letters)
letters.startswith('ALL') >>> True # ALL로 시작하는가?
letters.endswith('ALL') >>> False # ALL로 끝나는가?

.find # 오프셋 찾기
letter.find(word) >>> 73
letter.rfind(word) >>> 214 # 끝에서 부터
없을 시 -1 출력

.index # 오브셋 찾기 2
letter.index(word) >>> 73
letter.rindex(word) >>> 214 # 끝에서 부터
없을 시 오류 출력

.count()
letters.count('the') >>> 3

.isalnum()
letters.isalnum() >>> True # 알파벳과 숫자로만 있는가? (특수문자 있을시 False)


.capitalize()
letters.capitalize() >>> 첫 번째 단어 대문자
letters.title() >>> 모든 첫 글자 대문자
letters.upper() >>> 모든 글자 대문자
letters.lower() >>> 모든 글자 소문자
letters.swapcase() >>> 대문자는 소문자로 소문자는 대문자로

.center(30) >>> '   duck   '
.ljust(30) >>> 'duck   '
.rjust(30) >>> '   duck'

포매팅(보간)

옛 스타일
format_string % data
"Our cat %s weighs %s pounds" % ('cat', 'weight')#변수 가능 >>> 'Our cat cat weighs weight pounds' 

%s >>> 그대로
%12s >>> 12만큼 앞 여백
%+12s >>>> 12만큼 옆여백 숫자면 앞에 +
%-12s >>>> 12만큼 뒷여백 
%.3s >>> 앞에서 3글자만
%12.3 >>> 앞에서 3글자 + 앞에서 12여백

a = 'my %s'
arg = 'clam'
print(a % arg) >>> my clam

새 스타일
format_string.format(data) >>> '{}'.format(letters)

things = 'woodchunk'
place = 'lake'
'The {} is in the {}.'.format(thing, place) >>> 'The woodchuck is in the lake.'

'The {1} is in the {0}.'.format(place, thing) >>> 'The woodchuck is in the lake.' #순서 조절 가능

'The {thing} is in the {place}'.format(things = 'woodchunk', place = 'lake')

d = {'thing' : 'duck', 'place' : 'bathtub'}
'The {0[thing]} is in the {0[place]}.'.format(d) >>> 'The duck is in the bathtub.'
'The {d[thing]} is in the {d[place]}.'.format(d) >>> 미작동
'The {d[1]} is in the {d[0]}.'.format(d) >>> 미작동

{:10s} >>> 뒤에 여백
{:<10s} >>> 뒤에 여백
{:>10s} >>> 앞에 여백
{:^10s} >>> 좌우 여백
{:!^10s} >>> 여백대신 !로 채우기

최신 스타일 f- 문자열

f'The {thins} is in the {place}
f'The {thins.capitalize()} is in the {place.rjust(20)}
f'{thing =}, {place =}' >>> thin = 'wereduck', place = 'werepond'




