!pip3 install torch
!pip3 install torchvisio


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