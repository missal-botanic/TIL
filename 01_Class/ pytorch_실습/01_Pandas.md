
```py
df = pd.DataFrame(data)
df = pd.read_csv('data.csv') # CSV 파일 불러오기
df = pd.read_excel('data.xlsx', sheet_name='Sheet1') # 엑셀 파일 불러오기

df.head()  # 첫 5행을 확인
df.tail()
df.shape  # (행의 수, 열의 수)
df.columns  # 컬럼명 리스트
df.dtypes  # 각 컬럼의 데이터 타입
df.describe()  # 수치형 데이터의 요약 통계량
df.info()  # 전체적인 데이터 프레임 정보
df.sample(n=5)  # 랜덤으로 5행 선택
df['컬럼명'].unique()  # 특정 컬럼의 고유 값 리스트
```

### 외부 데이터 읽기
```py
df = pd.read_csv('example.csv')

url = 'https://example.com/data.csv'  # CSV 파일의 URL
data = pd.read_csv(url)

url = 'https://example.com/data.xlsx'  # Excel 파일의 URL
data = pd.read_excel(url)

```

# 시리즈(Series)

### 시리즈 클래스는 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 구조를 갖고 있습니다. 
```py
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])


print('시리즈의 값 : {}'.format(sr.values))
print('시리즈의 인덱스 : {}'.format(sr.index))
```

# 데이터 프레임(DataFrame)

### 데이터 프레임

```py
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)

       A  B  C
one    1  2  3
two    4  5  6
three  7  8  9
```
```py
df.index
Index(['one', 'two', 'three'], dtype='object')

df.columns
Index(['A', 'B', 'C'], dtype='object')
```

```py
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
```


### 리스트(List) 데이터프레임의 생성

```py
data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

      0         1      2
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14

pd.DataFrame(data, columns=['학번', '이름', '점수'])

     학번        이름     점수
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

### 딕셔너리(dictionary) 데이터프레임의 생성
```py
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

     학번        이름     점수
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

### 인덱스를 출력
```py
print(df.index)
출력 : RangeIndex(start=0, stop=6, step=1)
```