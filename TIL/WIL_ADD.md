```py
s = "abcdefghij"

print(s[0])
print(s[0:1])
a
a
```
```py
s = "I love apples"

print(s.replace("apples", "bananas"))

result = s.replace("apples", "bananas")
print(result)

I love bananas
I love bananas
```

```py
s = "Find the index of the first 'e' character"
s.find('e') #index() 없을 시 오류 find()는 -1
try:
    print(index('fja'))
except:
    print('error')

# list는 find 없음
# count 는 둘다
```

```py
s[-7:-3]
>>> 4567

```
```py
split() 참고 문자는 사라짐
```
```py
s = " OpenAI "
s.strip().upper() #strip은 양쪽 공백제거가 기본 값
s.strip()[1].upper() # 리스트일 경우 바로 선택

```
```py
print(s[0:len(s):1])
# print(s[::-1])
print(s[len(s)-1::-1])
```
```py
email = input('이메일 주소를 입력하세요: ')
email = email.strip().split('@')
email_id = email[0]
email_domain = email[-1]

print(email_id)
print(email_domain)
```
```py
s[::2] #홀수
s[1::2] #짝수
```
```py
# 01
email = input('이메일 주소를 입력하세요: ')
email = email.strip().split('@')
email_id = email[0]
email_domain = email[-1]
# 02
email_id, email_domain = email.strip().split('@') #객쳇가 같으면 '언패킹' 된다.

print(email_id)
print(email_domain)
```
```py
s = "dfskofg"

result = []
for a in range(len(s)):
    if a % 2 == 0:
        result.append(s[a])
print(result)
>>> ['d', 's', 'o', 'g']v

result = [s[a] for a in range(len(s)) if a % 2 == 0]
print(result)
>>> ['d', 's', 'o', 'g']
```
```py
join # 리스트에 해당
```
```py
words[len(words)-1] # =< > 이기 떄문에 =< >-1 이다.

my_list = [0, 1, 2, 3, 4, 5]
print(my_list[5:1:-1]) # end 부분 -1이다.
>>> [5, 4, 3, 2]
```

```

fruits = ['apple', 'banana', 'cherry']
fruits.append(['data','blueberry'])
print(fruits)
>>>
['apple', 'banana', 'cherry', ['data', 'blueberry']]

fruits = ['apple', 'banana', 'cherry', 'watermelon', 'date']
new_fruits = ['melon', 'blueberry']
fruits.extend(new_fruits)
print(fruits)
>>>
['apple', 'banana', 'cherry', 'watermelon', 'date', 'melon', 'blueberry']

fruits = ['apple', 'banana', 'cherry', 'watermelon', 'date']
new_fruits = ['melon', 'blueberry']

print(fruits + new_fruits)
>>> ['apple', 'banana', 'cherry', 'watermelon', 'date', 'melon', 'blueberry']
```

```
list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2 * 2)
>>> [1, 2, 3, 4, 5, 4, 5]
```


```
numbers.sort()
numbers.reverse()
numbers.sorted() 
sorted(numbers, reverse=True)
