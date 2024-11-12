
1. 단어 토큰화(Word Tokenization)

입력: Time is an illusion. Lunchtime double so!

출력 : "Time", "is", "an", "illustion", "Lunchtime", "double", "so"


### 토크나이져
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence

    Don't
    Don t
    Dont
    Do n't
    Jone's
    Jone s
    Jone
    Jones

#### word_tokenize
단어 토큰화1 : ['Do', "n't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr.', 'Jone', "'s", 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.']
Don't를 Do와 n't로 분리하였으며, 반면 Jone's는 Jone과 's로 분리

#### wordPunctTokenizer
단어 토큰화2 :'['Don', "'", 't', 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr', '.', 'Jone', "'", 's', 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.']  
Don't를 Don과 '와 t로 분리하였으며, 이와 마찬가지로 Jone's를 Jone과 '와 s로 분리

#### text_to_word_sequence
단어 토큰화3 : ["don't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', 'mr', "jone's", 'orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop']
don't나 jone's와 같은 경우 아포스트로피는 보존


토큰화에서 고려해야할 사항

1) 구두점이나 특수 문자를 단순 제외해서는 안 된다.
2) 줄임말과 단어 내에 띄어쓰기가 있는 경우.

규칙 1. 하이푼으로 구성된 단어는 하나로 유지한다.
규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다. 


### 표준 토큰화
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()
text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."

TreebankWordTokenizer : ['Starting', 'a', 'home-based', 'restaurant', 'may', 'be', 'an', 'ideal.', 'it', 'does', "n't", 'have', 'a', 'food', 'chain', 'or', 'restaurant', 'of', 'their', 'own', '.']

### Word2Vec
```py
from transformers import pipeline

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from scipy.spatial.distance import cosine

sentences =[
    "The sun set behind the mountains, painting the sky in shades of orange and purple."
    "She opened the old book and discovered a hidden letter inside.",
    "The gentle sound of waves crashing on the shore brought her peace.",
    "He decided to take a different route home to enjoy the beautiful scenery.",
    "The garden was filled with colorful flowers, attracting butterflies and bees.",
    ]

processed = [simple_preprocess(sentence) for sentence in sentences]

model = Word2Vec(sentences = processed, vector_size = 5, window = 5, min_count = 1, sg = 0)
dog = model.wv['home']
cat = model.wv['bees']

sim = 1 - cosine(dog, cat)
sim
```


### multilingual
```py
from sentence_transformers import SentenceTransformer
import numpy as np

# Multilingual-E5-large-instruct 모델 로드
model = SentenceTransformer('intfloat/multilingual-e5-large')
#model.save('./multilingual-e5-large')
# 문장 리스트
sentences = [
    '''이 영화를 본 건 꽤 오래로 을 당 열어젖히고 그곳을 떠난다.'''

]

# 문장들을 임베딩으로 변환
embeddings = model.encode(sentences)

# 임베딩 벡터 출력
print(embeddings.shape)  # (4, 1024) - 4개의 문장이 1024 차원의 벡터로 변환됨

print(embeddings[0]) 
```

### multilingual 로컬
```py
from sentence_transformers import SentenceTransformer
 
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
model.save('./tokenizer_multilingual')
Colored
```