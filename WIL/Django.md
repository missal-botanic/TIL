### 준비
```bash
conda create --name jg python=3.10 # 가상환경
```
### 설치
```bash
pip install django==4.2 # 장고 설치
```
### SQL(model) 설치
``` bash
'sqlite' # vscode익스텐션 설치

python manage.py migrate # 동기화 + 최초 한번은 마이그레이션 필요

control + shift + p -> sqlite 검색->sqlite OPEN DATABASE -> db.sqlite3 # 선택

SQLITE EXPLORER # 왼쪽 하단에  생김

# 새로운 열 생성시 빈공간 채우는 메시지 -> 1선택 -> 그냥 엔터 -> 자동 채움
# 마이그레션 파일 지울 경우 `__init__.py` 파일은 삭제하지 않도록 주의

```
shell 필요실 설치
```bash
# 장고 shell 설치
pip install django-extensions # 장고 익스텐션 설치 shell +
pip install ipython 

# 장고 shell 실행
python manage.py shell
python manage.py shell_plus # 기본 라이브러리 all load
```
```bash
# 파일첨부
pip install pillow
```
```bash
# 무작위 DB생성
pip install django-seed
pip install psycopg2
```
-----
### 새 프로젝트
```bash
# 1. 앱 생성 Bash

django-admin startproject {project_name} # 프로젝트 시작

django-admin startproject {project_name} . # 바닥에 파일 생성(추천)

rm - rf {project_name} # 설치 제거

cd my_first_pjt # 생성한 프로젝트 폴더로 이동
```
현재 루트에 view생성은 안되는것으로 보임 확인필요
### 실행
```bash
python manage.py runserver # 서버 실행
```
### 앱 생성
app 생성 - urls등록 - views등록 - template 폴더생성 - html 만들기

```bash

# 최상위폴더(manage.py와 같은 위치로 이동)
python manage.py startapp articles # 앱 (이름 복수형 권장)
python manage.py startapp users

mkdir apps/articles # app 파일 위치 변경시
python manage.py startapp articles apps/articles
```
```py
# 2. 앱 등록 settings.py 파일 33줄
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_seed',
    'rest_framework',
    # 서드파티 앱
    'articles', # <- 추가
    'users', # <- 추가
]

# 마지막에 "," Trailing commas

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # 상위 폴더 검색 범위 추가(현재는 base.html이 위치)
        'APP_DIRS': True, # 장고에게 앱 안쪽 경로 찾으라 지시(기본 값)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# USER author
AUTH_USER_MODEL = 'accounts.User'

# STATIC_URL 
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles" # 배포시 사용
STATICFILES_DIRS = [BASE_DIR / "static"] # 배포전에도 사용 가능하게

# Media files
MEDIA_URL = "/media/" 
MEDIA_ROOT = BASE_DIR / "media"


# BASE_DIR는 Django 프로젝트의 기본 디렉토리 경로를 나타내며, 보통 settings.py 파일이 위치한 곳입니다.
```
## accounts
```py
상속
# 루트 폴더 내에 templates + base.html 부모 만들기
# app 폴더 내에 templates + index.html 자식 만들기
# app 폴더 내에 urls.py 만들기
```
```py
### accounts / modesl
from django.contrib.auth.models import AbstractUser # 추가

class User(AbstractUser):
    pass
```
```py
# settings
AUTH_USER_MODEL = 'accounts.User'
```
```bash
python manage.py createsuperuser

python manage.py seed articles --number=30

python manage.py seed articles --number=20 --seeder "Comment.article_id" 1
```py
### urls.

```html
<!-- 루트 / templates / base -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static "css/style.css" %}}"> 
</head>
<body>
    {% load static %}

    {% block content %}
    {% endblock content %}
</body>
</html>
```

```html
<!-- apps / templates / index -->

{% extends "base.html" %}

{% block content %}
<p>index</p>
{% endblock content %}
```
```py
###  루트 / urls
from django.contrib import admin
from django.urls import path, include # include 추가
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name='index'), # 추가 views, index 위치는 app에
    path("articles/", include("articles.urls")),
    path("users/<str:username>/", views.users, name='users'),
    
]
```
```py
### articles / urls

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name = 'articles'),
]
```

## model

```py
### articles - models

from django.db import models

class Article(models.Model): # (모듈.클래스)
    title = models.CharField(max_length=50) 
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True) # 객체 처음 생성될 때 자동으로 현재 시간
    updated_at = models.DateTimeField(auto_now=True) # 객체가 수정될 때마다 자동으로 현재 시간

# models.Model은 Django 모델 클래스의 기반 클래스이고, models.CharField는 모델 필드의 하위 클래스
# 코드는 같고 용도의 차이
```

manage.py 와 같은 곳에서 실행
```bash
# 마이그레이션 : 파이썬 모델을 DB에 생성 준비
python manage.py makemigrations  # 생성

# 마이그레이션 : 파이썬 모델을 DB에 반영
python manage.py migrate  # 반영
```
```bash
db.sqlite3 파일 선택 -> control + shift + p -> sqlite 검색->sqlite OPEN DATABASE -> db.sqlite3 # 선택

SQLITE EXPLORER # 왼쪽 하단에  생김
```
```bash
# 방법01

article = Article() # 클래스로 객체 생성
article.title = 'first_title'  # 생성된 객체의 title 필드에 'first_title'을 할당
article.content = 'my_content' # 생성된 객체의 content 필드에 'my_content'를 할당
article.save() # save()하기전에는 저장되지 않음


# 방법02

article = Article(title='두번째 제목', content='두번째 내용')
article.save()


# 방법03

Article.objects.create(title='third title', content='세번째 내용') # save()가 필요하지 않는 방법
```
### articles
```py
### articles / urls

path('', views.articles, name = 'articles'),


### articles / views

def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles, # 출력시 전체 / 입력시 부분
    }
    return render(request, "articles.html", context)


### articles / template / articles

{% extends "base.html" %}

{% block content %}
<a href="{% url "new"%}">글쓰기</a>
    {% for article in articles %}
        <div>{{ article.id }}</div>
        <div>{{ article.title }}</div><br>
    {% endfor %}
{% endblock %}
```

### create
```py
### articles / urls

path('new/', views.new, name = 'new'), # 추가
path('create/', views.create, name = 'create'), # 추가


### articles / views

from django.shortcuts import render, redirect # redirect
from .models import Article # apps 내부 model의 Article 함수

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == "POST":
        title = request.POST.get("title") # Django의 HttpRequest 객체의 속성 중 하나
        content = request.POST.get("content")
        Article.objects.create(title = title, content = content)
        return redirect("articles")
    return redirect("articles")


### articles / template /html

<form action="{% url 'create' %}" method="POST"> # form
    {% csrf_token %}
 
    <label for = 'title'>제목</label>
    <input type='text' id='title' name='title'><br> # 'name' 중요

    <label for='content'>내용</label>
    <input type='text' id='content' name='content' cols='30' rows='10'><br> # 'name' 중요

    <button type='submit'>저장</button>
</form>
<a href = "">뒤로</a>
```
### article_detail
```py
### articles / urls

path('<int:pk>/article-detail/', views.article_detail, name ='article_detail'), # pk가 있으면 views.article_detail 에도 pk인수를 받음


### articles / views

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article,
    }
    return render(request, "article_detail.html", context)


### articles / html

<label for='title'>제목:</label>
<p>{{ article.title }}</p><br>
<label>내용</label>
<p>{{ article.content }}</p>

<a href="{% url "articles" %}">뒤로</a>

<form action ="{% url "delete" article.pk %}" method="POST">
    {% csrf_token %}
    <button type="submit">삭제</button>
</form>

<a href="{% url "edit" article.pk %}">수정</a>
```
### delete
```py
### articles / urls

path('<int:pk>/delete/', views.delete, name = 'delete'),


### articles / views

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(id=pk)
        article.delete()
        return redirect("articles")
    return redirect("articles_detail")


### articles / html

<form action ="{% url "delete" article.pk %}" method="POST">
    {% csrf_token %}
    <button type="submit">삭제</button>
</form>
```

### edit
```py
### articles / urls 

path('<int:pk>/edit/', views.edit, name = 'edit'),
path('<int:pk>/update', views.update, name = 'update'),


### articles / views

def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article
    }
    return render(request, "edit.html", context)

def update(request, pk):
    if request.method == "POST":
        article = Article.objects.get(id=pk)
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("article_detail", article.pk)
    return redirect("article_detail", article.pk)


### articles / html # created와 같은 모양의 페이지 필요

<form action="{% url 'update' article.pk %}" method="POST"> # views 만 있는 url
    {% csrf_token %}

    <label for = 'title'>제목</label>
    <input type='text' id='title' name='title' value = "{{article.title}}"><br> # title 미리 채워짐

    <label for='content'>내용</label>
    <input type='text' id='content' name='content' cols='30' rows='10' value="{{article.content}}"></input><br> # content 미리 채워짐

    <button type='submit'>수정</button>
</form>

<a href="{% url "articles" %}">뒤로</a>
```
# 전문
```py
### 로컬 / urls

from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('articles/', include("articles.urls")),
]


### articles / urls

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name = 'articles'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/article-detail/', views.article_detail, name ='article_detail'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update', views.update, name = 'update'),
]


### articles / views

from django.shortcuts import render, redirect
from .models import Article


def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles, 
    }
    return render(request, "articles.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title = title, content = content)
        return redirect("articles")
    return redirect("articles")

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article,
    }
    return render(request, "article_detail.html", context)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(id=pk)
        article.delete()
        return redirect("articles")
    return redirect("articles_detail")
    

def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article
    }
    return render(request, "edit.html", context)

def update(request, pk):
    if request.method == "POST":
        #print(request)
        #print(pk)
        article = Article.objects.get(id=pk)
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("article_detail", article.pk)
    return redirect("article_detail", article.pk)
```


```py
### 로컬 / base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% block content %}
    {% endblock content %}
</body>
</html>
```


```py
### articles / index

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>index</p>
</body>
</html>
```


```py
### articles / article.html

{% extends "base.html" %}

{% block content %}
<a href="{% url "new"%}">글쓰기</a>
    {% for article in articles %}
        <div>{{ article.id }}</div>

        <div> 
        <a href = "{% url "article_detail" article.pk %}"> {{ article.title }} </a> # 클릭시 이동
        </div><br>

    {% endfor %}
{% endblock %}
```

```py
### article / article_detail.html

{% extends "base.html" %}

{% block content %}

<label for='title'>제목:</label>
<p>{{ article.title }}</p><br>
<label>내용</label>
<p>{{ article.content }}</p>

<a href="{% url "articles" %}">뒤로</a>
<form action ="{% url "delete" article.pk %}" method="POST">{% csrf_token %}
<button type="submit">삭제</button>
</form>
<a href="{% url "edit" article.pk %}">수정</a>

{% endblock content %}
```


```py
### article / new.html

{% extends "base.html" %}

{% block content %}

<form action="{% url 'create' %}" method="POST">
    {% csrf_token %}
    <h2>new</h2>
    <label for = 'title'>제목</label>
    <input type='text' id='title' name='title'><br>

    <label for='content'>내용</label>
    <input type='text' id='content' name='content' cols='30' rows='10'><br>

    <button type='submit'>저장</button>
</form>
<a href = "">뒤로</a>

{% endblock %}
```

```py
### articles / edit

{% extends "base.html" %}

{% block content %}

<form action="{% url 'update' article.pk %}" method="POST">
    {% csrf_token %}
    <h2>new</h2>
    <label for = 'title'>제목</label>
    <input type='text' id='title' name='title' value = "{{article.title}}"><br>

    <label for='content'>내용</label>
    <input type='text' id='content' name='content' cols='30' rows='10' value="{{article.content}}"></input><br>

    <button type='submit'>수정</button>
</form>
<a href = "">뒤로</a>

{% endblock %}
```



