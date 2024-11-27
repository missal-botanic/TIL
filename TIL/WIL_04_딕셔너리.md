### 딕셔너리

항목의 순서를 따지지 않음

오프셋이 없다

키:값(쌍)

중괄호 속 들여쓰기는 가독성을 위한것

인수 이름이 공백과 예약어가 없는것

키들은 고유해야한다. 중복될 수 없다. 중복될 시 마지막내용 짤림


empty_dict = {}

dict(a = '1', b = '2', c  = '3') #?? 확인 필요
poem_dc = {'a' : 1, 'b' : 2, 'c' : 3}

list = [('a', 1),('b', 2),('c', 3)]
list = (['a', 1],['b', 2],['c', 3])
list = [['a', 1],['b', 2],['c', 3]]

dic = [list]
>>> [['a', 1], ['b', 2], ['c', 3]]



list = [ 'aaa', 'bbb', 'ccc' ] # -> 에러
list = [ 'aa', 'bb', 'cc' ]
dict(list)
>>> {'a': 'a', 'b': 'b', 'c': 'c'}

list_dc['a'] = 2 # 'a' 키의 값을 바꿈


list_dc['z'] >>> 없을 시 오류 호출
'z' in dict >>> False #미리 확인 가능

list_dc.get('a')
>>> 'A'

list_dc.get('z')
>>> # none 출력

dict.get('z', 'not in dict')
>>> not in dict # 없을 시 메시지 선택 가능

list_dc = {'a': '1', 'b': '2', 'c': '3'}
list_dc.keys()
>>> dict_keys(['a', 'b', 'c'])

list(list_dc.keys())
>>>  ['a', 'b', 'c']

list(list_dc.values())
>>> [1, 2, 3]

list(list_dc.items())
>>> [('a', 1), ('b', 2), ('c', 3)]

len() # 키값 쌍으로 개수
>>> 3



first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
{**first, **second}
>>> {'a': 'agony', 'b': 'bagels', 'c': 'candy'} # 얕은 복사 두 번째 딕셔너리 값 기준으로

third = {'d': 'donuts'}
{**first, **third, **second}
>>> {'a': 'agony', 'b': 'bagels', 'd': 'donuts', 'c': 'candy'} # 얕은 복사


first.update(second)
>>> {'a': 'agony', 'b': 'bagels', 'c': 'candy'}

.pop('a', 'no_key')
>>> 'no_key'

.clear() # 키, 값 모두 삭제

'a' in first
>>> True

first['e'] = '4'
first
>>> {'a': 'agony', 'b': 'bagels', 'c': 'candy', 'e': '4'} # 'e' 추가

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bliss', 'a': 'agony'}
first == second
>>> True # 순서는 상관없다. == 외에 쓰는것은 없다.

for letter in first.keys(): # 키

for letter in first.values(): # 값

for letter in first.items(): # 튜플로 반환
    print(letter)
>>> ('a', 'agony')
('b', 'bliss')

for letter room in first.items(): # 2개의 변수면 키, 값 각각 들어간다.


word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}
letter_counts
>>> {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)} # set() 추가
letter_counts
>>> 
{'r': 1, 'e': 2, 'l': 1, 's': 1, 't': 2}

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word if letter in word} #if 문 추가 set도 가능
letter_counts
>>> {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

