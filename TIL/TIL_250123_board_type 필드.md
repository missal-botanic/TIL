게시판 이름을 영어로 변경하는 방법은 모델의 필드와 관련된 이름을 변경하는 것뿐입니다. `Board` 모델에서 `board_type` 필드와 함께 사용되는 이름들을 영어로 바꾸겠습니다.

예를 들어, `자유게시판`은 `free board`, `질문게시판`은 `Q&A board`로 변경합니다.

### 수정된 모델 예시 (영어로 변경)

```python
from django.db import models

class Board(models.Model):
    # 게시판 유형을 고정된 값으로 지정하기 위해 choices를 사용
    FREE_BOARD = 'free'
    QNA_BOARD = 'qna'

    BOARD_TYPE_CHOICES = [
        (FREE_BOARD, 'Free Board'),
        (QNA_BOARD, 'Q&A Board'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    board_type = models.CharField(
        max_length=3,
        choices=BOARD_TYPE_CHOICES,  # 여기서 선택할 수 있는 값만 지정
        default=FREE_BOARD  # 기본값을 Free Board로 설정
    )

    def __str__(self):
        return f"{self.name} ({self.get_board_type_display()})"

    # board_type에 대응하는 텍스트를 더 가독성 있게 반환할 수 있도록 helper method 추가
    def get_board_type_display(self):
        return dict(self.BOARD_TYPE_CHOICES).get(self.board_type, 'Unknown')


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

### 변경된 내용:
1. **게시판 유형 `choices`**:
   - `FREE_BOARD` → `'Free Board'`
   - `QNA_BOARD` → `'Q&A Board'`

2. **`__str__()` 메서드**:
   - 게시판 이름과 함께 `board_type`을 사람이 읽을 수 있는 형태로 출력할 때 `"Free Board"`나 `"Q&A Board"`로 출력됩니다.

3. **기본값**:
   - `default=FREE_BOARD`로 설정하여 기본 게시판을 `Free Board`로 설정합니다.

### 마이그레이션 작업:
모델을 변경한 후에는 마이그레이션을 만들어야 합니다.

1. **마이그레이션 생성**:

```bash
python manage.py makemigrations
```

2. **마이그레이션 적용**:

```bash
python manage.py migrate
```

### 예시 데이터 추가:
이제 게시판을 추가할 때 영어로 게시판 유형을 지정할 수 있습니다.

```python
# Free Board 생성
free_board = Board.objects.create(name='Free Board', description='A board for general posts', board_type=Board.FREE_BOARD)

# Q&A Board 생성
qna_board = Board.objects.create(name='Q&A Board', description='A board for asking and answering questions', board_type=Board.QNA_BOARD)
```

### 출력 예시:

```python
board = Board.objects.get(id=1)
print(board)  # 출력: Free Board (Free Board)
```

이렇게 하면 게시판 이름과 유형을 영어로 구분할 수 있습니다.