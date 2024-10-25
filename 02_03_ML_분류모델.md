
### SVM( StandardScaler 표준편차, MinMaxScale 선택 )


1. Linear Kernel
선형 분리를 사용합니다. 데이터가 선형적으로 분리 가능할 때 적합합니다.
```
SVC(kernel='linear')
```
2. Polynomial Kernel
다항식 커널을 사용하여 비선형 분리를 수행합니다.
```
SVC(kernel='poly', degree=3) # 여기서 degree는 다항식의 차수
``` 
3. Radial Basis Function (RBF) Kernel
가장 일반적으로 사용되는 커널로, 비선형 문제에 잘 작동합니다. 데이터의 밀집 지역을 기준으로 결정 경계를 형성합니다.
```
SVC(kernel='rbf')
```
4. Sigmoid Kernel
신경망의 활성화 함수와 유사한 방식으로 작동하는 커널입니다. 비선형성을 모델링할 수 있지만, 일반적으로 성능이 좋지 않습니다.
```
SVC(kernel='sigmoid')
```
5. Custom Kernel
사용자가 정의한 커널 함수를 사용할 수 있습니다. 이 경우, 커널 함수를 직접 구현해야 합니다.
```
SVC(kernel=custom_kernel_function)
```
추가 옵션
C: 규제 파라미터로, 오분류에 대한 패널티를 조정합니다. 기본값은 1.0입니다.(하이퍼파라미터)
gamma: RBF 커널에 대한 파라미터로, 데이터 포인트의 영향 범위를 조정합니다. 낮은 값은 넓은 범위를, 높은 값은 좁은 범위를 의미합니다.
degree: Polynomial 커널의 차수를 설정합니다. 기본값은 3입니다.

```
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X = data.data
y = data.target

X_tr, X_te, y_tr, y_te = tts(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_tr = scaler.fit_transform(X_tr)
X_te = scaler.transform(X_te)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = SVC(kernel = 'linear', C=1)
model.fit(X_tr, y_tr)

pre_v = model.predict(X_te)

svc.score(X_te,y_te)
```

