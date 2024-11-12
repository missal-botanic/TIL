**Word2Vec**에서 단어끼리 유사도를 측정하는 방법은 **벡터 공간**을 기반으로 합니다. Word2Vec은 단어를 고차원 **벡터**로 표현하며, 이 벡터들은 **단어 간의 의미적 관계**를 반영하는 방식으로 학습됩니다. Word2Vec 모델에서 단어 간 유사도는 **벡터 간의 거리**나 **유사성**으로 측정할 수 있습니다. 일반적으로 사용되는 두 가지 방법은 **코사인 유사도**(Cosine Similarity)와 **유클리드 거리**(Euclidean Distance)입니다.

### 1. **Word2Vec의 기본 개념**

Word2Vec은 단어를 **고차원 벡터**로 매핑하는 모델입니다. 이 벡터들은 단어의 **의미적 유사성**을 반영하고, 비슷한 의미를 가진 단어들이 비슷한 벡터 값으로 매핑되도록 학습됩니다. Word2Vec에는 두 가지 주요 모델이 있습니다:

- **CBOW (Continuous Bag of Words)**: 문맥을 통해 중심 단어를 예측하는 방식.
- **Skip-gram**: 중심 단어를 통해 문맥 단어를 예측하는 방식.

이렇게 학습된 단어 벡터는 **단어 간의 관계**를 수치적으로 나타냅니다. 예를 들어, "king"과 "queen"의 벡터는 비슷한 의미를 갖고 있기 때문에 **벡터 공간에서 가까운 위치**에 있을 것입니다.

### 2. **단어 간 유사도 측정**

Word2Vec에서 두 단어 벡터 간의 유사도를 측정하는 데 가장 흔히 사용되는 방법은 **코사인 유사도**입니다. 코사인 유사도는 두 벡터가 이루는 **각도**에 기반하여 유사도를 계산합니다. 두 벡터가 비슷한 방향을 가질수록 유사도가 높습니다.

#### **코사인 유사도** 계산

코사인 유사도는 다음과 같은 수식으로 계산됩니다:

\[
\text{cosine similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
\]

- \( A \)와 \( B \)는 두 단어의 벡터입니다.
- \( A \cdot B \)는 두 벡터의 **내적**(dot product)입니다.
- \( \|A\| \)와 \( \|B\| \)는 각각 벡터의 **노름(norm)**입니다.

코사인 유사도는 두 벡터의 방향이 얼마나 유사한지를 나타내며, 값은 **-1**에서 **1** 사이입니다. 값이 **1**에 가까울수록 두 벡터는 매우 유사하고, **-1**에 가까울수록 매우 다릅니다. **0**은 두 벡터가 완전히 독립적임을 나타냅니다.

#### **유클리드 거리** (Euclidean Distance)
유클리드 거리는 두 벡터 간의 **직선 거리**를 계산하는 방법입니다. 유클리드 거리가 작을수록 두 벡터가 유사하다는 것을 의미합니다. 유클리드 거리는 다음과 같이 계산됩니다:

\[
\text{Euclidean distance}(A, B) = \sqrt{\sum_{i=1}^n (A_i - B_i)^2}
\]

### 3. **Python 예시 코드**

Word2Vec에서 단어 벡터를 사용하여 단어 간의 유사도를 계산하는 예시 코드입니다. `gensim` 라이브러리를 사용하여 Word2Vec 모델을 학습하고, 코사인 유사도를 계산하는 방법을 보여드립니다.

#### **단어 유사도 계산 예시 (Word2Vec)**

```python
import gensim
from gensim.models import Word2Vec

# 예시 문장 데이터
sentences = [
    ["i", "love", "machine", "learning"],
    ["machine", "learning", "is", "fun"],
    ["i", "love", "coding"],
    ["i", "enjoy", "learning", "new", "things"]
]

# Word2Vec 모델 학습
model = Word2Vec(sentences, min_count=1, vector_size=50, window=3)

# 단어 벡터 확인
vector_king = model.wv['king']
vector_queen = model.wv['queen']

# 두 단어 간 유사도 계산 (코사인 유사도)
similarity = model.wv.similarity('king', 'queen')

print(f"유사도 (King vs Queen): {similarity}")
```

### 4. **단어 유사도 계산 방법**

위 코드에서 `model.wv.similarity('king', 'queen')`는 `king`과 `queen` 간의 **코사인 유사도**를 계산합니다. `model.wv['king']`과 `model.wv['queen']`은 각각 `king`과 `queen`의 벡터를 반환합니다. 이 벡터들은 학습된 Word2Vec 모델에서 계산된 벡터입니다.

### 5. **Word2Vec을 사용하여 유사한 단어 찾기**

Word2Vec에서는 `most_similar` 메서드를 사용하여 특정 단어와 **유사한 단어**들을 찾을 수 있습니다.

```python
# 'king'과 유사한 단어 5개 찾기
similar_words = model.wv.most_similar('king', topn=5)

for word, similarity in similar_words:
    print(f"단어: {word}, 유사도: {similarity}")
```

이 코드는 `'king'`과 가장 유사한 단어 5개를 출력합니다. 이 방식은 **"king"과 비슷한 의미를 가진 단어들**을 벡터 공간에서 가까운 순서대로 찾아줍니다.

### 6. **결론**

Word2Vec은 단어들을 벡터 공간에 매핑하고, 벡터 간의 거리나 유사도를 계산하여 단어 간의 의미적 관계를 이해합니다. 가장 많이 사용되는 유사도 계산 방법은 **코사인 유사도**입니다. 이를 통해 우리는 단어들 간의 의미적 유사성을 계산하고, **유사한 단어**를 찾거나 **단어 간 관계**를 분석할 수 있습니다.