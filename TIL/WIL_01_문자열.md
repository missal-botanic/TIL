
### 3)텍스트 문자열

```
시퀀스 시스템
문자열은 불변

print() 출력은 인터프리터와 아이들과 출력방식이 다르다
아이들은 따움표가 생략되고 줄 바꿈은 \n 로 표시 된다.
```

```bash
\n 줄바꿈 
\t 띄어 쓰기 
"\"hi\""
\\ 는 실제 \ 표시
```



```py
"hello"+"baby" >>> 'hellobaby'
"hello""baby" >>> 'hellobaby'
('a' + "e" + '''i''' + """u""") >>> 'aeiu'
print('a' + "e" + '''i''' + """u""") >>> 'aeiu'
```

```py
a = 'a'
b = "e"
c = '''i'''
d = """u"""
print(a + b + c + d) >>> 'aeiu'
```

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

```py
letter[0] # 첫문자 선택

letter[0] = 'p' >>> # 오류 발생

letter.replace('H', 'P') # 함수 방식, 새롭게 값이 만들어진다. 원본 불변
'P' + letter[1:] # 슬라이스 방식
```

### 4)슬라이스

```
시작, 끝, 스텝
```

```
[:] 전체 [s:] s부터 끝까지 [:e] 시작부터 e-1 까지 [s:e:st] st만큼 건너 뛰면서
```

```
letters[-3:0] >>> 'xyz'
letters[-6:-2] >>> 'uvwx'
letters[::7] >>> 'ahov'
letters[::-1] = letters[-1::-1] >>> zyx...cba
letters[70:71] >>> ''
```



```
string.function(arguments) 메서드 기본 구조 ()안에서는 인수가 들어간다. 인수가 없을 시에도 ()는 들어간다.
```

```py
''.join()

letters = ['abc', 'def', 'hij']
new_letters = ','.join(letters) 
>>>'abc,def,hij'
```

```py
.split()

letters = "abc, def, hij"
letters.split(",") >>> ['abc', 'def', 'hij']
```

```py
.replace()

letters.replace('a', 'b') # a를 b로 바꾼다.
letters.replace('a', 'b', 100) # 100회 까지 바꾼다.
```

```py
.strip() # 맨 앞 or 맨 뒤 ' ', \n , \t 자동 제거
.lstrip() # 왼쪽(시작)만 제거
.rstrip() # 오른쪽(끝)만 제거

letter('!') # !가 없으면 아무 일도 일어나지 않는다 #?? 확인필요.

"hello....!!!?" .strip('.!?') >>> "hello"
```

```py
import string

string.whitespace >>> ' \t\n\r\x0b\x0c'
string.punctuation >>> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

letters.strip(string.whitespace + string.punctuation)# 앞선 호출은 확인용
```

```py
len(letters)
letters.startswith('ALL') >>> True # ALL로 시작하는가?
letters.endswith('ALL') >>> False # ALL로 끝나는가?
```

```py
.find # 오프셋 찾기
letter.find(word) >>> 73
letter.rfind(word) >>> 214 # 끝에서 부터
없을 시 -1 출력

.index # 오브셋 찾기 2
letter.index(word) >>> 73
letter.rindex(word) >>> 214 # 끝에서 부터
없을 시 오류 출력
```

```py
.count()
letters.count('the') >>> 3 # 몇번 나오는지

.isalnum()
letters.isalnum() >>> True # 알파벳과 숫자로만 있는가? (특수문자 있을시 False)
```

```py
.capitalize()
letters.capitalize() >>> 첫 번째 단어 대문자
letters.title() >>> 모든 첫 글자 대문자
letters.upper() >>> 모든 글자 대문자
letters.lower() >>> 모든 글자 소문자
letters.swapcase() >>> 대문자는 소문자로 소문자는 대문자로
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
"Our cat %s weighs %s pounds" % ('cat', 'weight') #변수 가능 >>> 'Our cat cat weighs weight pounds' 
```

```bash
%s >>> 그대로
%12s >>> 12만큼 앞 여백
%+12s >>>> 12만큼 옆여백 숫자면 앞에 +
%-12s >>>> 12만큼 뒷여백 
%.3s >>> 앞에서 3글자만
%12.3 >>> 앞에서 3글자 + 앞에서 12여백
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
'The {} is in the {}.'.format(thing, place) >>> 'The woodchuck is in the lake.'

'The {1} is in the {0}.'.format(place, thing) >>> 'The woodchuck is in the lake.' #순서 조절 가능

'The {thing} is in the {place}'.format(things = 'woodchunk', place = 'lake')
```

```py
d = {'thing' : 'duck', 'place' : 'bathtub'}
'The {0[thing]} is in the {0[place]}.'.format(d) >>> 'The duck is in the bathtub.'
'The {d[thing]} is in the {d[place]}.'.format(d) >>> 미작동
'The {d[1]} is in the {d[0]}.'.format(d) >>> 미작동
```

```bash
{:10s} >>> 뒤에 여백
{:<10s} >>> 뒤에 여백
{:>10s} >>> 앞에 여백
{:^10s} >>> 좌우 여백
{:!^10s} >>> 여백대신 !로 채우기
```

### 최신 스타일 f- 문자열

```py
thins = pen
place = desk

f'The {thins} is in the {place}
f'The {thins.capitalize()} is in the {place.rjust(20)}

f'{thing =}, {place =}' >>> thin = 'wereduck', place = 'werepond'
```

```
r"" 원시 문자열\n 은 내용 그대로 전부 출력 하지만 print() 구문은 이스케이프 적용되어 출력
```