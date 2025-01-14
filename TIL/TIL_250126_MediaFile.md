Django에서 사용자 프로필 이미지와 다른 이미지들을 구분해서 저장하려면, **모델**을 설계할 때 각 이미지의 저장 경로를 별도로 설정할 수 있습니다. 기본적으로 **Django 모델**에서 이미지 필드를 사용할 수 있으며, `ImageField`를 사용하면 됩니다. 이때 각 이미지를 다른 폴더에 저장하려면 `upload_to` 속성을 활용할 수 있습니다.

여기서는 **사용자 프로필 이미지**와 **기타 이미지**를 구분하여 저장하는 방법을 설명하겠습니다.

### 1. **프로필 이미지와 사용자 이미지를 구분하는 모델 설계**

`User` 모델에 **프로필 이미지**를 추가하고, 또 다른 모델(예: **Article** 또는 **Post**)에 **사용자 이미지**를 추가하는 방법을 설명합니다.

#### `accounts/models.py` - **사용자 프로필 이미지**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 프로필 이미지를 저장할 필드
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.username
```

- `upload_to='profile_images/'`로 설정하여 프로필 이미지를 `MEDIA_ROOT/profile_images/`에 저장합니다.
- `null=True`와 `blank=True`로 설정하여 프로필 이미지가 선택 사항임을 나타냅니다.

#### `articles/models.py` - **게시글에 포함된 사용자 이미지**
```python
from django.db import models
from apps.accounts.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    # 게시글에 첨부할 사용자 이미지
    user_image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

- `upload_to='user_images/'`로 설정하여 이미지가 `MEDIA_ROOT/user_images/`에 저장됩니다.

### 2. **`settings.py`에서 미디어 파일 경로 설정**

`settings.py`에서 **미디어 파일** 경로를 설정해야 합니다. 사용자가 업로드한 이미지는 이 경로에 저장됩니다.

```python
# 미디어 파일 경로 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- `MEDIA_URL`: 실제 URL에서 미디어 파일에 접근할 수 있도록 설정합니다.
- `MEDIA_ROOT`: 업로드된 파일들이 실제로 저장될 로컬 디렉터리 경로입니다. 예를 들어, 프로젝트 루트 디렉터리에 `media/` 폴더가 생성됩니다.

### 3. **URL 설정**

`urls.py`에서 미디어 파일을 제공할 수 있도록 설정합니다. 개발 환경에서는 Django가 미디어 파일을 제공할 수 있도록 `urlpatterns`에 추가해야 합니다.

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    # 기존의 URL 패턴들...
]

# 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 4. **템플릿에서 이미지 표시하기**

HTML 템플릿에서 이미지를 표시하려면 `{% load static %}` 태그를 사용하여, `profile_image`와 같은 필드에서 이미지를 불러올 수 있습니다.

#### 예시: 사용자 프로필 이미지 표시
```html
<img src="{{ user.profile_image.url }}" alt="Profile Image" />
```

#### 예시: 게시글에서 사용자 이미지 표시
```html
<img src="{{ article.user_image.url }}" alt="User Image" />
```

### 5. **이미지 업로드 테스트**

Django의 **Admin** 인터페이스를 사용하거나 **Django shell**을 통해 프로필 이미지 및 게시글 이미지를 업로드하고, 경로가 올바르게 저장되는지 확인할 수 있습니다.

### 6. **추가적인 필드 설정**

각 모델에서 이미지를 추가로 저장하려면 `ImageField`의 `upload_to` 옵션을 다르게 지정하여 다른 폴더에 저장할 수 있습니다. 예를 들어, 게시글에 여러 이미지가 첨부될 수 있다면:

```python
# 게시글 모델에서 여러 이미지를 첨부하는 경우
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    images = models.ManyToManyField('ArticleImage', related_name='articles')

class ArticleImage(models.Model):
    image = models.ImageField(upload_to='article_images/')
    caption = models.CharField(max_length=255)
```

- 이 경우 `Article` 모델은 여러 개의 `ArticleImage`를 가질 수 있으며, `ArticleImage`는 `article_images/` 폴더에 이미지를 저장합니다.

### 결론

- **프로필 이미지**와 **기타 사용자 이미지**는 `upload_to` 속성을 사용하여 저장 위치를 다르게 설정할 수 있습니다.
- `MEDIA_URL`과 `MEDIA_ROOT`를 설정하여 이미지 파일을 관리하고, Django의 템플릿에서 이를 불러와서 표시할 수 있습니다.
