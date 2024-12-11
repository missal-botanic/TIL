"Weight 업데이트가 학습이다"는 기계 학습, 특히 딥러닝에서 핵심적인 개념을 나타냅니다. 다음은 이에 대한 설명입니다:

    가중치(Weight): 딥러닝 모델의 가중치는 입력 데이터에 대한 중요성을 결정하는 파라미터입니다. 모델은 이 가중치를 조정하여 입력과 출력 사이의 관계를 학습합니다.

    학습 과정: 모델은 주어진 데이터셋을 통해 패턴을 학습합니다. 이 과정에서 예측값과 실제값 간의 오차(손실)를 계산하고, 이 손실을 최소화하는 방향으로 가중치를 업데이트합니다.

    최적화 알고리즘: 주로 경량 하강법(Gradient Descent) 같은 최적화 알고리즘을 사용하여 가중치를 조정합니다. 이 알고리즘은 손실 함수의 기울기를 계산하고, 그 기울기에 따라 가중치를 조금씩 수정해 나갑니다.

    반복적 학습: 이러한 가중치 업데이트는 여러 번 반복되며, 각 반복(에폭)마다 모델의 성능이 향상됩니다. 모델이 데이터에 잘 맞도록 가중치를 조정하는 것이 바로 학습의 핵심입니다.

결국, "weight 업데이트가 학습이다"는 모델이 데이터로부터 경험을 통해 가중치를 조정하여 더 나은 예측을 할 수 있도록 하는 과정을 강조하는 표현입니다.

_ 가 있는 현제 변수가 바뀜

broadcasting 

img_t = torch.randn(3, 5, 5) # 채널, x사이즈, y사이즈 크기를 가진 랜덤 텐서
batch_t = torch.randn(2,3,5,5) # 배치 크기 2, 채널 3, 높이와 너비가 5
weight = torch.tensor([0.2126 0.7152, 0.0722]) # RGB 채널에 대한 가중치 값, 일반적으로 이미지의 밝기를 계산할 때 사용
weight.shape

unsqueezed_weights = weights.unsqueez(-1).unsqueez_(-1) # unsqueeze(-1): 텐서의 마지막 차원에 새로운 차원을 추가합니다. 따라서 (3,)는 (3, 1)이 됩니다.
# unsqueeze_(-1): 동일한 방식으로 마지막에 또 하나의 차원을 추가하여 (3, 1)을 (3, 1, 1)로 변환합니다.
unsqueezed.shape

Select a mini-batch of data (of size bs)
batch는 부분적으로 학습하는 개념과 메모리에 얼마나 데이터를 올리는지를 결정한다

use the model to make prediction
calculate the loss

로스율에 따라 그레디언트 분석
Backward pass: loss.backword() updates the gradient of the model.

그레디언트 따라 웨이트 선정 (옵티마이져 따라 진행 방법 다름)
Weight update: Have the optimizer take a step in toward lower loss

쓴 그레디언트느 버린다.
Zero ant old gradients.


torch nn
https://github.com/pytorch/pytorch


https://github.com/torch/nn
https://pytorch.org/docs/stable/nn.html

### 레이어

Linear

Convolutional

Recurrent

### Activation funtion

다양한 활성화 함수(Activation Function)가 있으며, 각각의 특징과 사용되는 경우가 다릅니다. 주요 활성화 함수는 다음과 같습니다:

### 1. Sigmoid
- **정의**: S자 형태의 곡선으로, 출력값이 0과 1 사이로 제한됩니다.
- **사용처**: 주로 이진 분류 문제의 출력층에서 사용.
- **단점**: 기울기 소실(vanishing gradient) 문제 발생 가능.

### 2. Tanh (Hyperbolic Tangent)
- **정의**: 출력값이 -1과 1 사이로 제한됩니다.
- **사용처**: 은닉층에서 주로 사용, Sigmoid보다 더 나은 성능을 보임.
- **단점**: 여전히 기울기 소실 문제 발생 가능.

### 3. ReLU (Rectified Linear Unit)
- **정의**: 0보다 작은 값은 0으로, 0보다 큰 값은 그대로 반환.
- **사용처**: 현대 신경망의 대부분의 은닉층에서 사용.
- **장점**: 기울기 소실 문제 해결, 계산이 간단.
- **단점**: 죽은 ReLU 문제(일부 뉴런이 0을 반환하여 학습되지 않음).

### 4. Leaky ReLU
- **정의**: 0보다 작은 값에 작은 기울기(예: 0.01)를 부여하여 반환.
- **사용처**: ReLU의 단점을 보완하기 위해 사용.
- **장점**: 죽은 ReLU 문제 완화.

### 5. Softmax
- **정의**: 다중 클래스 분류에서 사용되며, 각 클래스에 대한 확률을 반환.
- **사용처**: 출력층에서 다중 클래스 분류 문제에 사용.
- **특징**: 출력값의 합이 1이 되도록 조정.

### 6. Swish
- **정의**: \( f(x) = x \cdot \text{sigmoid}(x) \) 형태로, 출력이 입력값과 sigmoidal 변환의 곱으로 정의됨.
- **사용처**: ReLU를 대체할 수 있는 활성화 함수로, 최근 연구에서 성능 향상.
- **장점**: 기울기 소실 문제 완화, 더 부드러운 그래디언트.

### 7. GELU (Gaussian Error Linear Unit)
- **정의**: 입력값을 가우시안 분포에 기반하여 활성화.
- **사용처**: 최신 모델(예: Transformer)에서 사용.
- **장점**: 신경망의 성능 향상.

### 8. PReLU (Parametric ReLU)
- **정의**: Leaky ReLU의 변형으로, 음수 구간의 기울기를 학습 가능한 파라미터로 설정.
- **장점**: 모델이 더 많은 유연성을 가질 수 있음.

이 외에도 다양한 활성화 함수가 있으며, 각 함수는 특정 상황이나 데이터에 따라 장단점이 있습니다. 모델의 성능을 극대화하기 위해 적절한 활성화 함수를 선택하는 것이 중요합니다.

**시그모이드 미분으로 작은 숫자화 문제가 생긴다. 그래서 렐루를 쓴다.**


### Loss functon

MSE # 다른것으로 인식하는것을 확인(제곱합 거리)
Logsoftmax + NLL # 핵심만 보자
CrossEntropy # 

one hot vector?
체인룰?


제곱합 거리(Sum of Squared Differences, SSD) 또는 제곱 오차(Squared Error)는 주로 회귀 분석, 기계 학습, 이미지 처리 등에서 사용되는 손실 함수입니다. 제곱합 거리를 사용하는 이유는 다음과 같습니다:
1. 비선형성 감소

제곱합 거리는 각 데이터 포인트와 모델의 예측 값 사이의 차이를 제곱하여 계산합니다. 이렇게 하면 음수와 양수의 차이를 모두 양수로 만들고, 차이의 크기를 강조합니다. 즉, 큰 오차에 더 큰 가중치를 부여하여 모델이 큰 오류를 줄이는 데 집중하도록 합니다.
2. 미분 가능성

제곱합 거리는 미분 가능하므로 경량화(Backpropagation)와 같은 최적화 알고리즘에서 유용합니다. 미분을 통해 기울기를 계산하고, 이 기울기를 바탕으로 파라미터를 업데이트할 수 있습니다.
3. 통계적 해석

제곱합 거리는 최대우도 추정(Maximum Likelihood Estimation)과 관련이 있습니다. 일반적으로 가정하는 노이즈가 정규 분포를 따른다고 할 때, 제곱합 거리를 최소화하는 것은 해당 데이터에 대한 최적의 선형 모델을 찾는 것과 같습니다.
4. 제어 용이성

제곱합 거리는 간단하고 직관적입니다. 손실 값을 쉽게 해석할 수 있으며, 다양한 상황에서 적용하기 쉽습니다.
5. 오류의 제곱 평균

제곱합 거리의 평균은 평균 제곱 오차(Mean Squared Error, MSE)로 불리며, 이는 모델의 전반적인 성능을 평가하는 데 매우 유용합니다. MSE는 예측과 실제 값 간의 차이의 제곱의 평균으로, 모델의 정확도를 측정하는 데 널리 사용됩니다.
요약

제곱합 거리는 오차를 효과적으로 강조하고, 미분 가능하며, 통계적 해석이 가능해 여러 머신러닝 및 통계 모델에서 널리 사용됩니다. 이러한 특성 덕분에 모델 학습과 최적화에 있어 강력한 도구가 됩니다.

### 빌드 방법
1. Use nn.Sequential
2. Subclass nn.Module

### torch.optim
다음은 PyTorch에서 제공하는 주요 최적화 알고리즘인 `torch.optim`의 종류입니다:

### 1. **SGD (Stochastic Gradient Descent)**
- **설명**: 일반적인 경량 최적화 기법으로, 전체 데이터셋이 아닌 랜덤하게 선택된 샘플(미니배치)을 사용하여 파라미터를 업데이트합니다.
- **특징**: 모멘텀(momentum)과 Nesterov 모멘텀을 지원하여 학습 속도를 높일 수 있습니다.

### 2. **Adam (Adaptive Moment Estimation)**
- **설명**: 모멘텀과 RMSprop의 장점을 결합한 알고리즘입니다. 각 파라미터에 대해 학습률을 적응적으로 조정합니다.
- **특징**: 메모리 요구량이 낮고 빠른 수렴을 보입니다.

### 3. **RMSprop (Root Mean Square Propagation)**
- **설명**: 각 파라미터에 대해 학습률을 조정하여 기울기의 변화에 따라 적응적으로 학습률을 조정하는 기법입니다.
- **특징**: 비등방성 손실 함수에 효과적이며, 수렴 속도가 빠릅니다.

### 4. **Adagrad (Adaptive Gradient Algorithm)**
- **설명**: 각 파라미터에 대해 학습률을 조정하여 자주 업데이트되는 파라미터의 학습률을 줄이고 드물게 업데이트되는 파라미터의 학습률을 늘립니다.
- **특징**: 특정 파라미터에 대한 학습률이 점점 감소하기 때문에, 훈련이 진행됨에 따라 더 많은 조정이 필요할 수 있습니다.

### 5. **Adadelta**
- **설명**: Adagrad의 단점을 보완하기 위해 개발된 기법으로, 학습률의 감소를 피하고 적응형 학습률을 지속적으로 유지합니다.
- **특징**: 이전의 그래디언트 정보에 기반하여 업데이트를 진행하며, 파라미터의 최적화에 효과적입니다.

### 6. **AdamW**
- **설명**: Adam의 변형으로, L2 정규화를 더 효율적으로 적용하여 weight decay를 지원합니다.
- **특징**: 파라미터 업데이트에 weight decay를 적용해 과적합을 방지하는 데 유리합니다.

### 7. **NAdam (Nesterov-accelerated Adam)**
- **설명**: Adam에 Nesterov 모멘텀을 결합한 알고리즘입니다.
- **특징**: 더 빠른 수렴을 보일 수 있으며, 깊은 신경망 훈련에 효과적입니다.

### 8. **FTRL (Follow The Regularized Leader)**
- **설명**: 온라인 학습에서 주로 사용되는 알고리즘으로, 이전의 모든 경험을 고려하여 파라미터를 업데이트합니다.
- **특징**: 일반화 성능을 높이기 위한 정규화 방법을 포함합니다.

### 9. **LBFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno)**
- **설명**: 2차 최적화 방법으로, 제한된 메모리에서 BFGS 알고리즘을 사용하여 경량으로 구현된 것입니다.
- **특징**: 적은 수의 파라미터로도 정확한 수렴을 보일 수 있습니다.

### 10. **ASGD (Averaged Stochastic Gradient Descent)**
- **설명**: SGD의 변형으로, 파라미터의 평균을 유지하여 더 안정적인 업데이트를 제공합니다.
- **특징**: 일반적으로 더 빠른 수렴을 보여주는 경향이 있습니다.

### 11. **Rprop (Resilient Backpropagation)**
- **설명**: 기울기의 부호만을 사용하여 업데이트를 수행하는 알고리즘입니다.
- **특징**: 기울기의 크기를 무시하고, 파라미터의 업데이트를 더 효율적으로 처리합니다.


### dataset/data_loader

Structure:(Date, Groundtruth)
Batch(N * ...)
    Tabular(N.C)
    2D image(N,C,H,W)
    3D image(N,C,D,H,W)
    Time-series data(N,C,L)

Data split
    Trianing
    Validation (일반화)
    Testing


### 원핫 벡터(One-Hot Vector) 
주로 범주형 데이터를 수치형으로 변환할 때 사용되는 표현 방식입니다. 각 범주를 고유한 이진 벡터로 나타내며, 다음과 같은 특징이 있습니다:

1. **구조**: 원핫 벡터는 특정 범주에 해당하는 인덱스만 1로 설정하고, 나머지 인덱스는 0으로 설정합니다. 예를 들어, 세 가지 범주(예: 빨강, 초록, 파랑)가 있을 경우:
   - 빨강: \([1, 0, 0]\)
   - 초록: \([0, 1, 0]\)
   - 파랑: \([0, 0, 1]\)

2. **차원**: 원핫 벡터의 차원은 범주 수와 동일합니다. 각 범주는 하나의 차원으로 표현되므로, 범주의 수가 많아질수록 벡터의 차원도 커집니다.

3. **사용 목적**: 원핫 인코딩은 머신러닝 모델에서 범주형 변수를 처리할 때, 거리 기반 알고리즘이나 신경망 모델에 입력하기 위해 주로 사용됩니다. 이러한 표현 방식은 모델이 각 범주 간의 관계를 잘 학습할 수 있도록 도와줍니다.

4. **장점**: 범주 간의 순서나 크기를 부여하지 않으므로, 범주형 데이터에 적합합니다. 예를 들어, "사과", "바나나", "체리"라는 범주를 단순한 정수로 표현하는 것보다 원핫 인코딩을 사용하면 이들 사이의 관계를 잘 반영할 수 있습니다.

5. **단점**: 원핫 벡터는 메모리 사용이 비효율적일 수 있습니다. 범주의 수가 많아지면 벡터의 차원이 증가하고, 이는 계산 복잡성을 높일 수 있습니다. 이 때문에, 대규모 범주를 가진 데이터에서는 다른 인코딩 방식(예: 임베딩)을 사용하는 것이 일반적입니다.


수학
확률
통계

COMMAND
파이썬
라이브러리
머신러닝
딥러닝
토치
nn토치
활용

api

미분 편미분 체인룰
정형(숫자)
비정형(이미지, 텍스트, 오디오)