`np.random` 모듈에는 다양한 랜덤 데이터 생성 함수가 있습니다. 몇 가지 주요 명령어를 소개하겠습니다:

### 1. **`np.random.rand(d0, d1, ..., dn)`**
- **설명**: 0과 1 사이의 균일 분포에서 샘플링한 난수로 구성된 배열을 생성합니다.
- **예시**: `np.random.rand(2, 3)`는 2x3 배열을 생성합니다.

### 2. **`np.random.randn(d0, d1, ..., dn)`**
- **설명**: 평균이 0이고 표준편차가 1인 정규 분포에서 샘플링한 난수 배열을 생성합니다.
- **예시**: `np.random.randn(2, 3)`는 2x3 배열을 생성합니다.

### 3. **`np.random.randint(low, high=None, size=None)`**
- **설명**: 주어진 범위에서 랜덤 정수를 생성합니다. `high`가 지정되지 않으면 `low`까지의 정수입니다.
- **예시**: `np.random.randint(1, 10, size=(2, 3))`는 1과 9 사이의 랜덤 정수로 구성된 2x3 배열을 생성합니다.

### 4. **`np.random.uniform(low, high, size=None)`**
- **설명**: 지정된 범위 내에서 균일 분포에 따라 난수를 생성합니다.
- **예시**: `np.random.uniform(1, 10, size=(2, 3))`는 1과 10 사이의 랜덤 실수로 구성된 2x3 배열을 생성합니다.

### 5. **`np.random.choice(a, size=None, replace=True, p=None)`**
- **설명**: 주어진 배열 `a`에서 랜덤하게 샘플링합니다. `replace`를 False로 설정하면 중복 없이 샘플링합니다.
- **예시**: `np.random.choice([1, 2, 3, 4, 5], size=3, replace=False)`는 1에서 5 사이의 숫자를 중복 없이 3개 선택합니다.

### 6. **`np.random.shuffle(x)`**
- **설명**: 배열 `x`의 원소들을 랜덤하게 섞습니다. 반환값은 없으며, 입력 배열이 변경됩니다.
- **예시**: 
  ```py
  arr = np.array([1, 2, 3, 4, 5])
  np.random.shuffle(arr)  # arr이 랜덤하게 섞임
  ```
