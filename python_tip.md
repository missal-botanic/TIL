
### python 버전확인
python --version

### pytorch 버전 호환 확인
https://pytorch.org/get-started/locally/
https://pytorch.org/get-started/previous-versions/

### pytorch cpu 버전일 때 설치
https://aka.ms/vs/17/release/vc_redist.x64.exe?utm_source=pytorchkr&ref=pytorchkr

### torchtext 버전 호환 확인
https://pypi.org/project/torchtext/

### 코랩 토치 설치
```
!pip3 install torch
!pip3 install torchvision
```

### 간편 설치 예제
```
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 cpuonly -c pytorch

conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 torchtext==0.17.0 cpuonly -c pytorch
```

### 설치 제거
```
pip uninstall torch torchvision torchaudio torchtext
```

### CPU GPU 차이
```
cpu : conda install pytorch torchvision torchaudio cpuonly -c pytorch
nvidia : conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
```

conda activate pandas_course
jupyter notebook

df.head()
df.sample(n=5)

df.describe()

## 결손값 확인
print(df.isnull().sum())

## 결손값 대처
df = df.dropna()
df['content'] = df['content'].fillna(df['content'].mode()[0]) #최반값
df['age'] = df['age'].fillna(df['age'].median()) #중앙값

### 하나의 열 선택
single_column = df['content']  # Series 형태

### 여러 열 선택
multiple_columns = df[['content', 'processed_review']]  # DataFrame 형태

### 기본적인 열 처리 함수
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

### map or apply 처리 함수
df['processed_review'] = df['content'].map(preprocess_text)
df['processed_review'] = df['content'].apply(preprocess_text)

df['alive'] = df['alive'].map({'no': 1, 'yes': 0})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2,})

### 특정 열 만 선택
df = df[['content', 'score']]

### Pandas
기본은 행 axis=0 
X = df.drop('data') #는 열이기 떄문에 axis=1 자동 인식
X = df.drop('sdata', axis=1) #가독성을 위해 명시적으로 표시



conda create --name pandas_course #콘다 가상 설치
conda activate pandas_course #콘다 가상 활성화
.venv/Script/active
conda deactivate #콘다 가상 비활성화

#콘다 가상 비활성화
pip install ipykernel
python -m ipykernel install --user --name pandas_course --display-name "pandas_course"


```
python -m venv venv
```
2. 보기 = 명령 팔렛트 -> "env" ->파이썬 가상환경 -> venv 만들기 -> 루트선정 ->버전선정
```
.venv/Scripts/activate
```


print(not a)    # False

x = 10
x = x + 10
x
와
x += 10
같다

비트연산자?

python -m venv venv

.venv/Script/active
pip install notebook
jupyter notebook

이터레이터


conda install pandas
pip install numpy
pip install jupyter
jupyter notebook
--가상 공간 보이게 하기--


conda env list
conda list

data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 35],
    '직업': ['학생', '회사원', '프리랜서']
}
길이가 같아야 한다

df = pd.DataFrame(data)
df["이름"][0]

inpace= 영구 변환
그냥 set 한번 변환

복합 /= 은 안되도 a=a/n은 될 수 있다.

~반대조건

기본값은 오름 차순 ascending = False 내림차순으로

!pip install matplotlib