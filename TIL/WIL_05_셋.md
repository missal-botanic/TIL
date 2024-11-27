자료구조
============

### 셋

null, empty 존재

empty = set() # {}는 이미 딕셔너리가 사용

even_number = {0, 2, 4, 6, 8}
odd_number = {1, 3, 5, 7, 9}

set( 'letters' ) # 문자열
>>> {'e', 'l', 'r', 's', 't'}

set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']) # 리스트
>>> {'Dancer', 'Dasher', 'Mason-Dixon', 'Prancer'}

set(('Ummagumma', 'Echoes', 'Atom Heart Mother')) # 듀플
>>> {'Atom Heart Mother', 'Echoes', 'Ummagumma'}

set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}) # 딕셔너리
>>> {'apple', 'cherry', 'orange'} # 키만 사용


```py
data = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])

len(data)
>>> 4

data.add(4)
>>> {4, 'Dancer', 'Dasher', 'Mason-Dixon', 'Prancer'} # 순서는 자동

data.remove('Dancer')
>>> {4, 'Dasher', 'Mason-Dixon', 'Prancer'}

for item in data:
    print(item)
>>>4
Mason-Dixon
Prancer
Dasher
```


in + .index()

```py
drinks = {
'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'},
'white russian': {'cream', 'kahlua', 'vodka'},
'manhattan': { 'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
>>>martini
black russian
white russian
screwdriver


for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
>>>black russian
screwdriver

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}: # & 연산자는 교집합을 구하는 연산자. 두 집합 간의 교집합을 구합니다.교집합이 비어 있지 않으면 해당 음료 이름을 출력하는 조건
        print(name)
>>>martini
manhattan
screwdriver

```

```py
bruss = drinks['black russian']
wruss = drinks['white russian']
bruss
>>>{'kahlua', 'vodka'}

a = {1, 2}
b = {2, 3}

a & b # 교집합
a.intersection(b)
>>> {2}

bruss & wruss
>>>{'kahlua', 'vodka'}

a | b # 합집합
a.union(b)
>>> {1, 2, 3}

bruss | wruss
{'cream', 'kahlua', 'vodka'}

a - b # 차집합
a.difference(b)
>>> {1}

bruss - wruss
>>> set()

wruss - bruss
>>> {'cream'}

a ^ b # 대칭 차집합
a.symmetric_difference(b)
>>> {1, 3}

wruss ^ bruss
>>> {'cream'}

a <= b # 부분 집합
a.issubset(b)
>>> False

bruss <= wruss
>>> True

a >= b # 상위 집합
a.issuperset(b)
>>> False

wruss >= bruss
>>> True


```

```py
frozenset([3, 2, 1])
frozenset(set([2,1,3]))
frozenset({3, 1, 2})
frozenset((2, 3, 1))
>>> frozenset({1, 2, 3}) # 이셋은 더 이상 변하지 않는다. .add() 를 실행하면 오류가 생긴다.
```

```py
data_list[2]
data_tuple[2]
data_dict[2]
if 'apple' in data_set: # 셋은 찾아야한다.
```

```py
f2e = {}
for word, mean in e2f.items():
    f2e[mean] = word
f2e
>>> {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}

```

life = {
    'animals' : ['cats', 'octopi', 'emus'],
    'plants' : ['Henri', 'Grumpy', 'Lucy'],
    'other' : []
}


life = {
    'animals': {
        'cats': ['Heri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}



life['animals']['cats'] # 값 출력

squares = {key: key*key for key in range(10)} # 딕셔너리 안에서 컨프리핸션

odd = {number for number in range(10) if number % 2 == 1}
>>> {1, 3, 5, 7, 9}

for thing in ('Got %s' % number for number in range(10)):
              print(thing)
>>> Got 0
Got 1
Got 2
Got 3
Got 4
Got 5
Got 6
Got 7
Got 8
Got 9



keys = ('a', 'b', 'c')
values = ('1', '2', '3')
dict(zip(keys, values))
>>> {'a': '1', 'b': '2', 'c': '3'}