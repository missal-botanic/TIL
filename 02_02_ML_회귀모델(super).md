회귀모델(super)
=============

## 변수 하나
선형 회귀 # 1차원 (선)
다항 회귀 # 2차원 이상 (곡선)

## 변수 다수 (동시에 돌리고 선택)
L2 릿지 회귀 # 제곱값 합 - 수식적
L1 랏소 회귀 # 절대값 합 - 비슷한 스케일


### 선형 회귀 모델

```py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5],[6,6]])
y = np.array([1, 2, 3, 4, 5, 6])

X_tr, X_te, y_tr, y_te = tts(X, y, test_size=0.2,random_state=42)

model = LR()
model.fit(X_tr, y_tr)

pre_v = model.predict(X_te)

print(mean_squared_error(y_te, pre_v))
print(r2_score(y_te, pre_v))
```

### 다항 회귀 (drgree 조절가능)
```py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([1, 4, 9, 16, 25, 36])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
```

### 리지 라쏘 회귀 (규제 조절 가능 (alpha=0.1))
```py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # plt 임포트 추가
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error as MSE, r2_score as r2

X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
y = np.array([1, 2, 3, 4, 5, 6])

X_tr, X_te, y_tr, y_te = tts(X, y, test_size=0.2, random_state=42)

#RG=Ridge(alpha=0.1)
#RG.fit(X_tr,y_tr)
#LS=Lasso(alpha=0.1)
#LS.fit(X_tr,y_tr)
```


