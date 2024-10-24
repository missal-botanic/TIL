### train_test_split
```
from sklearn.model_selection import train_test_split
```
기능: 데이터를 학습용(train)과 테스트용(test)으로 나누는 함수입니다.
용도: 모델의 성능을 평가하기 위해 데이터를 두 개의 세트로 분리합니다. 일반적으로 test_size를 지정하여 테스트 세트의 비율을 설정합니다. 이를 통해 과적합(overfitting)을 방지할 수 있습니다.


### StandardScaler
```
from sklearn.preprocessing import StandardScaler
```
기능: 데이터의 표준화를 수행하는 클래스입니다.
용도: 특성(feature)의 평균을 0, 표준편차를 1로 조정하여 데이터의 스케일을 통일합니다. 이는 특히 거리 기반 알고리즘이나 선형 모델에서 성능을 향상시킬 수 있습니다.


### LogisticRegression
```
from sklearn.linear_model import LogisticRegression
```
기능: 로지스틱 회귀(Logistic Regression) 모델을 생성하는 클래스입니다.
용도: 이진 분류 문제에 사용되며, 독립 변수와 종속 변수 간의 관계를 모델링합니다. 예를 들어, Titanic 데이터에서 승객의 생존 여부를 예측하는 데 사용할 수 있습니다.

### accuracy_score
```
from sklearn.metrics import accuracy_score
```
기능: 모델의 정확도를 계산하는 함수입니다.
용도: 실제 클래스와 예측한 클래스 간의 일치 비율을 계산하여 모델의 성능을 평가합니다. 정확도는 (올바르게 예측한 샘플 수) / (전체 샘플 수)로 정의됩니다.

### classification_report
```
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다

### classification_report
```
from sklearn.metrics import classification_report
```
기능: 분류 모델의 성능을 상세히 평가하는 함수입니다.
용도: 정확도, 정밀도(precision), 재현율(recall), F1 점수 등 다양한 성능 지표를 포함하여 출력합니다. 이는 클래스 불균형이 있는 데이터셋에서 모델의 성능을 더 잘 이해하는 데 도움이 됩니다.