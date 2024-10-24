### set() 은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
```
s1 = set([1,2,3])
print(s1)
```
result : {1,2,3}

```
s2 = set("hello")
print(s2)
```
result : {'o', 'h', 'l', 'e'}

만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트 or 튜플로 변환한 후 해야 한다.
```
s1 = set([1,2,3])

l1 = list(s1)
print(l1)		# result : [1,2,3]
print(l1[0])		# result : 1

t1 = tuple(s1)
print(t1)		# result : (1,2,3)
print(t1[0])		# result : 1
```

## set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

### 교집합
& 기호를 사용하여 교집합 구하기
s3 = s1 & s2
print(s3)	#result : {4,5,6}
intersection()을 사용하여 교집합 구하기
s3 = s1.intersection(s2)
print(s3)	#result : {4,5,6}

### 합집합
| 기호를 사용하여 합집합 구하기
s3 = s1 | s2
print(s3)	#result : {1, 2, 3, 4, 5, 6, 7, 8, 9}
union()을 사용하여 합집합 구하기
s3 = s1.union(s2)
print(s3)	#result : {1, 2, 3, 4, 5, 6, 7, 8, 9}

### 차집합
차집합을 구할 때는 어떤 집합이 앞에 오느냐에 따라 값이 달라진다.

-를 사용하여 차집합 구하기
s3 = s1 - s2
print(s3)	#result : {1, 2, 3}

s3 = s2 - s1
print(s3)	#result : {8, 9, 7}
difference()를 사용하여 차집합 구하기
s3 = s1.difference(s2)
print(s3)	#result : {1, 2, 3}

s3 = s2.difference(s1)
print(s3)	#result : {8, 9, 7}

## 집합 자료형 관련 함수들

### 값 1개 추가히기(add)
이미 만들어진 set 자료형에 값을 추가할 수 있다.
s1 = set([1,2,3])
s1.add(4)
print(s1)	#result : {1, 2, 3, 4}

### 값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)	#result : {1, 2, 3, 4, 5, 6}

### 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)	#result : {1, 3}