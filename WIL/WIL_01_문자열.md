#### 생성
```
words = "letters"
```
#### 확인
```
letter[0]

.find()
.rfind()

.index()
.rindex()

len()
.startswith('ALL')
.endswith('ALL')
.isalnum()

.count('the')
```
#### 수정
```
''.join()
.split('')

.replace()

.strip()
.lstrip()
.rstrip()

a + b + c + d
"hello""baby"
'a' + "e" + '''i''' + """u"""

.capitalize()
.title()
.upper()
.lower()
.swapcase()

.center(30)
.ljust(30)
.rjust(30)

name, "님의 ", age, "입니다." 
"%s님의 %s살입니다" % (name, age) 
"{0}님의 {1}살입니다.".format(name, age) 
f"{name}님의 나이는 {age}살입니다."

sep="", end="" 
```
복합 수정
```
result = original[:5] + "Beautiful" + original[5:]

result = "".join([original[:5], "Beautiful", original[5:]])

리스트화 + original_list[5:5] = ['Beautiful']

리스트화 + insert(5, "Beautiful")+ ''.join(original_list)

```
### 텍스트 문자열

```
시퀀스 시스템
문자열은 불변

print() 출력은 인터프리터와 아이들과 출력방식이 다르다
아이들은 따움표가 생략되고 줄 바꿈은 \n 로 표시 된다.
```

```
string.function(arguments) 메서드 기본 구조 ()안에서는 인수가 들어간다. 인수가 없을 시에도 ()는 들어간다.
```
출력
```bash
\n 줄바꿈 
\t 띄어 쓰기 
"\"hi\""
\\ 는 실제 \ 표시
```
### 생성


```py
start = 'Na' * 4 + '\n'
middle = 'hey' * 3 + '\n'
end = 'Goodbye'

print(start + start + middle + end)
>>>NaNaNaNa
NaNaNaNa
heyheyhey
Goodbye # 줄바꿈보다 *이 더 높은 우선순위
```

### 확인(선택)
```py
letter = "pppp"

letter[0] # 첫문자 선택

letter[0] = 'H' 
>>> 오류 발생 # 문장열은 변경 불가능

new_letter = letter.replace('p', 'H') # 함수 방식, 새롭게 값이 만들어진다. 원본 불변
# (new_letter = ) 정의 꼭 필요
>>> HHHH

new_letter = 'H' + letter[1:] # 슬라이스 방식
>>> Hppp
```

슬라이스

```py
(시작 : 끝 : 스텝) # 음수 가능
```

```py
[:] # 전체
[s:] # s부터 끝까지 
[:e] # 시작부터 e-1 까지 
[s:e:st] # st만큼 건너 뛰면서
```

```py
letters = "abcdefghijklmnopqrstuvwxyz"

letters[-3:0] 
>>> 'xyz'

letters[-6:-2] 
>>> 'uvwx'

letters[::7] 
>>> 'ahov'

letters[::-1] = letters[-1::-1] 
>>> 'zyx...cba'

letters[70:71] 
>>> ''

```

```py
.find # 오프셋 찾기

letter.find(word) # 값이 없을 시 아무 일도 일어나지 않는다.
>>> 73

letter.rfind(word) # 끝에서 부터
>>> 214 

# 없을 시 -1 출력

.index 

letter.index(word)  # 오브셋 찾기 2
>>> 73

letter.rindex(word) # 끝에서 부터
>>> 214 

# 없을 시 오류 출력
```
```py
len(letters) # 문자열 길이 출력
```
```py
.startswith

letters.startswith('ALL') >>> True # ALL로 시작하는가?

.endswith

letters.endswith('ALL') >>> False # ALL로 끝나는가?

.isalnum()
letters.isalnum() >>> True # 알파벳과 숫자로만 있는가? (특수문자 있을시 False)
```

```py
.count()
letters.count('the') >>> 3 # 몇번 나오는지

```

### 수정
```py
''.join() # 리스트를 합치는 함수 (문자열 -> 리스트)

letters = ['abc', 'def', 'hij']
new_letters = ','.join(letters) 
>>>'abc,def,hij'
```

```py
.split() # 리스트로 분할 하는 함수 (리스트 -> 문자열)

letters = "abc, def, hij"
letters.split(",") >>> ['abc', 'def', 'hij']
```

```py
.replace()

letters.replace('a', 'b') # a를 b로 바꾼다.
letters.replace('a', 'b', 100) # 100회 까지 바꾼다.
```

```py
.strip() # 맨 앞 or 맨 뒤 ' ', \n , \t (자동 제거)

.lstrip() # 왼쪽(시작)만 (자동 제거)
.rstrip() # 오른쪽(끝)만 (자동 제거)

"hello....!!!?" .strip('.!?') >>> "hello" # 선택 제거
```
```py
a = 'a'
b = "e"
c = '''i'''
d = """u"""

print(a + b + c + d) 
>>> 'aeiu'
```
```py
print("hello"+"baby") 
>>> 'hellobaby'

print("hello""baby") 
>>> 'hellobaby'

print('a' + "e" + '''i''' + """u""") 
>>> 'aeiu'
```

```py
# 라이브리러 사용
import string

string.whitespace >>> ' \t\n\r\x0b\x0c'
string.punctuation >>> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

letters.strip(string.whitespace + string.punctuation) # letters에 적용
```

```py
.capitalize()

letters.capitalize()
>>> 첫 번째 단어 대문자

letters.title() 
>>> 모든 첫 글자 대문자

letters.upper()
>>> 모든 글자 대문자

letters.lower()
>>> 모든 글자 소문자

letters.swapcase()
>>> 대문자는 소문자로 소문자는 대문자로
```

```py
.center(30) >>> '   duck   '
.ljust(30) >>> 'duck   '
.rjust(30) >>> '   duck'
```

### 포매팅(보간)

옛 스타일

```
format_string % data
```

```py
"%s" % (,)

"Our cat %s weighs %s pounds" % ('cat', 'weight') #변수 가능 >>> 'Our cat cat weighs weight pounds' 
```

```bash
%s 
>>> 그대로

%12s 
>>> 12만큼 앞 여백

%+12s 
>>> 12만큼 옆여백 숫자면 앞에 +

%-12s 
>>> 12만큼 뒷여백 

%.3s 
>>> 앞에서 3글자만

%12.3 
>>> 앞에서 3글자 + 앞에서 12여백
```

```py
a = 'my %s'
arg = 'clam'
print(a % arg) >>> my clam
```

### 새 스타일

```
format_string.format(data) >>> '{}'.format(letters)
```

```py
things = 'woodchunk'
place = 'lake'
'The {} is in the {}.'.format(thing, place) 
>>> 'The woodchuck is in the lake.'

'The {1} is in the {0}.'.format(place, thing) 
>>> 'The woodchuck is in the lake.' #순서 조절 가능

'The {thing} is in the {place}'.format(things = 'woodchunk', place = 'lake')
```

```py
d = {'thing' : 'duck', 'place' : 'bathtub'}

'The {0[thing]} is in the {0[place]}.'.format(d)  # 0은 format 순서
>>> 'The duck is in the bathtub.'

'The {d[thing]} is in the {d[place]}.'.format(d) 
>>> 미작동

'The {d[1]} is in the {d[0]}.'.format(d) 
>>> 미작동
```

```py
{:10s} 
>>> 뒤에 여백

{:<10s} 
>>> 뒤에 여백

{:>10s} 
>>> 앞에 여백

{:^10s} 
>>> 좌우 여백

{:!^10s} 
>>> 여백대신 !로 채우기
```

### 최신 스타일 f- 문자열

```py
thing = 'pen'
place = 'desk'

f'The {thins} is in the {place}

f'The {thins.capitalize()} is in the {place.rjust(20)}

f'{thing =}, {place =}' #  = 는 변수 이름과 값을 함께 출력하라는 의미
>>> thing ='pen', place ='desk'
```

```
r"" 원시 문자열\n 은 내용 그대로 전부 출력 하지만 print() 구문은 이스케이프 적용되어 출력
```

```py
print(name, "님의 나이는", age, "살입니다.") # 띄어 쓰기 문제
print("%s님의 나이는 %s살입니다" % (name, age)) # "" 안에 구별 없이
print("{0}님의 나이는 {1}살입니다.".format(name, age)) # "" 안에 구별 없이, + {} 0 부터 시작

print(f"{name}님의 나이는 {age}살입니다.") #안에 구별 없이, + {}
>>>'우왁굳 님의 나이는 30 살입니다.'
```

```py
a = 10
b = 5
print(f"a + b = {a + b}") # 연산자 가능
>>>
a + b = 15
```


```py
r = int(input("원의 반지름을 입력하세요"))

print(f"원의 넓이는 { r * 3.14 * 2}입니다.")
>>> '원의 반지름을 입력하세요 30'
'원의 넓이는 188.4입니다.'
```
```py
# 올바른 사용법
try:
    r = int(input("원의 반지름을 입력하세요: "))
    print(f"반지름은 {r}입니다.")
except ValueError: # ValueError 생략 가능
    print("잘못된 입력입니다. 정수를 입력하세요.")
```

```py
# 01
map(function, iterable)

def f(x):
    return x + 5

numlist = [1, 2, 3, 4, 5]

print(f(numlist)) f 함수
>>> 오류

# 02
templist = []

for i in numlist:
    templist.append(f(i)) # for + f() 함수

print(templist)
>>>
[6, 7, 8, 9, 10]

print(map(f, numlist)) # map 함수 잘못된 함수
>>>
<map object at 0x000002080820C310> # 

print(list(map(f, numlist))) # map 함수
>>>
[6, 7, 8, 9, 10]

```
```py
phone_number = "010-1111-2222"

phone_number_splited = phone_number.split('-')
" ".join(phone_number_splited)
>>>
'010 1111 2222'

phone_number1 = phone_number.replace("-", " ")
>>>
'010 1111 2222'

phone_number[3] = 2
>>> 오류 replace로 해야함
```
```py
url = "http://sharebook.kr"
url[-2:]
>>>
'kr'
```

print 함수 sep="", end="" 
```py
print('naver','kakao','sk','samsung', sep=";") # sep=";" 나누는 기준
>>>
naver;kakao;sk;samsung

print("first", end=""); print("second") # end="" 자동 줄바꿈 제거
>>>
firstsecond
```
```
a, b, c = map(int, input().split())
```