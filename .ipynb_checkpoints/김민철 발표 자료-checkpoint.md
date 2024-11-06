# TIL


### keras 방식으로 학습 테스트
> Keras는 딥러닝 모델을 쉽게 구축하고 훈련할 수 있도록 돕는 고수준의 API로, 텐서플로우와 같은 백엔드 위에서 작동합니다.

```py

# ------------------------------------- 필요한 라이브러리 임포트 생략 ------------------------------------

# 파일 불러오기
df = pd.read_csv("netflix_reviews.csv")  

# 텍스트 전처리 함수
def preprocess_text(text):
    if isinstance(text, float):
        return ""
    text = text.lower()  # 대문자를 소문자로 변환
    text = re.sub(r'[^\w\s]', '', text)  # 구두점 제거
    text = re.sub(r'\d+', '', text)  # 숫자 제거
    text = text.strip()  # 양쪽 공백 제거
    return text

# 점수 카운트 계산
score_counts = df['score'].value_counts().reset_index()
score_counts.columns = ['Score', 'Count']

# 텍스트 토큰화
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['content'])
X = tokenizer.texts_to_sequences(df['content'])
X = pad_sequences(X)

# 레이블 설정
y = df['score'].values

# 학습 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=42)

# 모델 정의
model = Sequential()
model.add(Dense(64, activation="relu", input_shape=(X_train.shape[1],)))
model.add(Dropout(0.1))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="linear"))  # 회귀를 위해 'linear' 활성화 함수 사용

model.compile(loss="mean_squared_error", optimizer="adam", metrics=["mae"])

# 모델 훈련
model.fit(X_train, y_train, epochs=10, batch_size=4, verbose=1)

# ------------------------------------------- 중간 생략 -------------------------------------------

Epoch 9/10
23427/23427 [==============================] - 45s 2ms/step - loss: 2.9106 - mae: 1.5832
Epoch 10/10
23427/23427 [==============================] - 47s 2ms/step - loss: 2.9105 - mae: 1.5832

<keras.src.callbacks.History at 0x28b7e82c760>

733/733 [==============================] - 1s 2ms/step
Accuracy: 10.547658684423956%


```
<span style="color:red"> 학습률 10% </span>

#### 요약

- 간결한 코드 구조 덕분에 동일한 데이터셋으로 학습을 시도했으나, 낮은 학습률을 보였습니다.
- 이는 Keras에 대한 이해 부족이 원인일 수 있으나, PyTorch에 비해 훨씬 간단하여 딥러닝 수준의 코드가 오류 없이 작동하는 점은 긍정적입니다.
- 따라서 Keras에 대한 심층적인 학습을 위해 별도의 시간을 할애할 필요가 있다고 생각합니다.


### 1차 기본 학습

```py

# ------------------------------------------- 중간 생략 -------------------------------------------

# 데이터 로더 정의
BATCH_SIZE = 16

# 손실 함수와 옵티마이저 정의
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 학습률 설정

# LSTM 모델 정의
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim, dropout_rate=0.5):
        super(LSTMModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers=2, batch_first=True, dropout=dropout_rate)  
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout_rate)  # 드롭아웃 레이어

    def forward(self, text):
        embedded = self.embedding(text)
        output, (hidden, cell) = self.lstm(embedded.unsqueeze(1))  # 배치 차원 추가
        hidden = self.dropout(hidden[-1])  # 드롭아웃 적용
        return self.fc(hidden)

# ------------------------------------------- 중간 생략 -------------------------------------------

Epoch 6, Loss: 1.4112727279465251
Epoch 7, Loss: 1.4057372415535927
Epoch 8, Loss: 1.3953191742201765
Epoch 9, Loss: 1.3764440944643788
Epoch 10, Loss: 1.352955166198948
Accuracy: 47.15499210312887%
```

<span style="color:red"> 학습률 47%  </span>

#### 요약

- 기본적으로 제시된 과제 조건에 충실하여 기본 코드를 작성했습니다.
- 드롭아웃을 적용하여 모델의 과적합을 방지하려고 했습니다.
- 미니배치 학습을 통해 모델의 성능을 개선하려고 노력했습니다.




### 2차 배치 사이즈 및 에폭 수 증가

```py
BATCH_SIZE = 64  # 배치 사이즈를 64로 설정

num_epochs = 100  # 학습할 에폭 수 조정 가능

# ------------------------------------------- 중간 생략 -------------------------------------------

Epoch 97, Loss: 1.1228876022348633
Epoch 98, Loss: 1.1235658764025458
Epoch 99, Loss: 1.1214616659965124
Epoch 100, Loss: 1.1203884350561852
Accuracy: 54.420113544201136%
```
<span style="color:red"> 학습률 54% </span>

#### 요약
- 배치 사이즈를 대폭 늘려보았습니다. 이는 모델의 학습 안정성을 향상시키고, 파라미터 업데이트의 변동성을 줄이는 데 도움이 됩니다.
- 에포크 수를 늘려보았습니다. 이는 모델이 데이터에 더 잘 적합하도록 하여 학습 성능을 향상시키는 데 기여할 수 있습니다.


### 3차 2레이어 추가

```py

#레이어 추가

# LSTM 모델 정의
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super(LSTMModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.lstm1 = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.lstm2 = nn.LSTM(hidden_dim * 2, hidden_dim, batch_first=True, bidirectional=True) 
        self.fc1 = nn.Linear(hidden_dim * 2, hidden_dim) 
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, text):
        embedded = self.embedding(text)
        lstm_out, (hidden, cell) = self.lstm1(embedded.unsqueeze(1))
        lstm_out, (hidden, cell) = self.lstm2(lstm_out)

        # 양방향의 hidden state를 결합
        hidden_cat = torch.cat((hidden[-2], hidden[-1]), dim=1)

        return self.fc2(self.fc1(hidden_cat))

# ------------------------------------------- 중간 생략 -------------------------------------------
Epoch 90, Loss: 1.1628416655413527
Epoch 91, Loss: 1.1616355441942963
Epoch 92, Loss: 1.1602509196300963
Epoch 93, Loss: 1.1576813772676748
Epoch 94, Loss: 1.1575369658730543
Epoch 95, Loss: 1.153783379601944
Epoch 96, Loss: 1.1520104497365984
Epoch 97, Loss: 1.150690621483448
Epoch 98, Loss: 1.1507031974938948
Epoch 99, Loss: 1.1478193214728971
Epoch 100, Loss: 1.1457121307125677
Accuracy: 56.00375634951125%

```

<span style="color:red"> 학습률 56% </span>

#### 요약

- LSTM 레이어가 1개에서 2개로 늘어나고, 각 레이어가 양방향으로 구성됨에 따라 모델의 복잡성이 증가했습니다.
- FC 레이어도 1개에서 2개로 증가하여 출력층으로의 연결이 더 세분화되었습니다.


### 4차 4레이어 추가

```py
# LSTM 모델 정의 (4 레이어)
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super(LSTMModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.lstm1 = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.lstm2 = nn.LSTM(hidden_dim * 2, hidden_dim, batch_first=True, bidirectional=True)
        self.lstm3 = nn.LSTM(hidden_dim * 2, hidden_dim, batch_first=True, bidirectional=True)  # 추가된 레이어
        self.lstm4 = nn.LSTM(hidden_dim * 2, hidden_dim, batch_first=True, bidirectional=True)  # 추가된 레이어
        self.fc1 = nn.Linear(hidden_dim * 2, hidden_dim)  # 첫 번째 완전 연결층
        self.fc2 = nn.Linear(hidden_dim, output_dim)  # 최종 출력층

    def forward(self, text):
        embedded = self.embedding(text)
        lstm_out, (hidden, cell) = self.lstm1(embedded.unsqueeze(1))
        lstm_out, (hidden, cell) = self.lstm2(lstm_out)
        lstm_out, (hidden, cell) = self.lstm3(lstm_out)  # 3번째 LSTM 레이어
        lstm_out, (hidden, cell) = self.lstm4(lstm_out)  # 4번째 LSTM 레이어

        # 양방향의 hidden state를 결합
        hidden_cat = torch.cat((hidden[-2], hidden[-1]), dim=1)

        return self.fc2(self.fc1(hidden_cat))


Epoch 1, Loss: 1.4411939945644079
Epoch 2, Loss: 1.438289221480438
Epoch 3, Loss: 1.4380339547635752

# ------------------------------------------- 중간 생략 -------------------------------------------

Epoch 18, Loss: 1.4378050892019434
Epoch 19, Loss: 1.4376814013048245
Epoch 20, Loss: 1.437378289349657
Epoch 21, Loss: 1.4371888463407654
Epoch 22, Loss: 1.43679916533187
Epoch 23, Loss: 1.4355940978681676
Epoch 24, Loss: 1.4332314667034474

```

<span style="color:red"> 학습의 정체 </span>

- 이 모델은 4개의 LSTM 레이어로 구성되어 있어 더 깊고 복잡한 구조를 가지고 있으며, 각 레이어는 양방향으로 설계되어 있어 더 많은 정보를 학습할 수 있는 가능성이 높습니다.
- FC 레이어는 이전 코드와 같지만, LSTM 레이어의 추가로 인해 모델의 표현력이 증가하고, 더 복잡한 패턴을 학습할 수 있게 됩니다.
- 하지만 레이어 수가 많아져 모델이 지나치게 복잡해져서 학습이 어려워진 것으로 보입니다. 필요 이상의 파라미터가 많으면 수렴하기 어려울 수 있음을 알게 되었습니다.


### 5차 2레이어 복구 및 옵티마이저 변경

```py

#옵티마이저의 학습률을 0.01에서 0.05로 변경했습니다

optimizer = optim.SGD(model.parameters(), lr=0.05)

# ------------------------------------------- 중간 생략 -------------------------------------------
Epoch 93, Loss: 1.0482210473802716
Epoch 94, Loss: 1.0486159132609187
Epoch 95, Loss: 1.046645594578961
Epoch 96, Loss: 1.0441050273159664
Epoch 97, Loss: 1.0450137004103677
Epoch 98, Loss: 1.0456044204405956
Epoch 99, Loss: 1.0434317154282189
Epoch 100, Loss: 1.0428769397247366
Accuracy: 61.032142399795106%

```

<span style="color:red"> 학습률 61% </span>


- 학습률이 증가하면, 가중치 업데이트가 더 커져서 손실 함수의 최소값에 더 빠르게 도달할 수 있습니다. 이로 인해 모델이 더 빨리 수렴할 수 있습니다.

- 특정 문제에서는 높은 학습률이 모델이 다양한 지역 최솟값을 탐색하는 데 도움을 줄 수 있습니다. 더 큰 업데이트로 인해 모델이 더 다양한 매개변수 공간을 탐색하게 됩니다.

- 초기 에포크에서 손실 값이 빠르게 감소할 수 있으며, 이는 모델이 더 효과적으로 학습하고 있다는 신호일 수 있습니다.

- 특정 데이터셋이나 모델 구조에서는 높은 학습률이 오히려 성능을 개선할 수 있습니다. 특히 LSTM과 같은 복잡한 모델에서는 일부 파라미터에 대해 더 큰 변화가 도움이 될 수 있습니다.