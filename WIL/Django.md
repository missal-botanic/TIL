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
sqlite # 익스텐션 설치

python manage.py migrate # 동기화 + 최초 한번은 마이그레이션 필요

control + shift + p -> sqlite 검색->sqlite OPEN DATABASE -> db.sqlite3 # 선택

SQLITE EXPLORER # 왼쪽 하단에  생김

# 새로운 열 생성시 빈공간 채우는 메시지 -> 1선택 -> 그냥 엔터 -> 자동 채움
# 마이그레션 파일 지울 경우 `__init__.py` 파일은 삭제하지 않도록 주의

```
shell 필요실 설치
```bash
pip install django-extensions # 장고 익스텐션 설치 shell +
pip install ipython 
```
```bash
python manage.py shell
python manage.py shell_plus # 기본 라이브러리 all load
```
-----
### ㅇ새 프로젝트
```bash
# 1. 앱 생성 Bash

django-admin startproject {project_name} # 프로젝트 시작

django-admin startproject {project_name} . # 바닥에 파일 생성

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
# BASE_DIR는 Django 프로젝트의 기본 디렉토리 경로를 나타내며, 보통 settings.py 파일이 위치한 곳입니다.
```
```py
상속
# 루트 폴더 내에 templates + base.html 부모 만들기
# app 폴더 내에 templates + index.html 자식 만들기
# app 폴더 내에 urls.py 만들기

```
### urls.
루트 - templates -  base.html 파일
```html
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
apps - templates - index.html 파일
```html
{% extends "base.html" %}

{% block content %}
<p>index</p>
{% endblock content %}
```
article - urls.py 파일
```py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name = 'articles'),
]
```
루트 - urls 파일
```py
  path("articles/", include("articles.urls")) -> path("articles/", include("articles.urls"))
 ```
```py
from django.contrib import admin
from django.urls import path, include # include 추가
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name='index'), # 추가 views, index 위치는 app 아래에
    #path("users/<str:username>/, views.users, name='users')
    path("articles/", include("articles.urls")),
]
```
## model
```bash
python manage.py makemigrations  # 생성
python manage.py migrate  # 반영

```
apps - models.py 파일
```py
class Article(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
manage.py 와 같은 곳에서 실행
```bash
# 마이그레이션 : 파이썬 모델을 DB에 생성 준비
python manage.py makemigrations  # 생성
```
```bash
# 마이그레이션 : 파이썬 모델을 DB에 반영
python manage.py migrate  # 반영

db.sqlite3 파일 선택 -> control + shift + p -> sqlite 검색->sqlite OPEN DATABASE -> db.sqlite3 # 선택

SQLITE EXPLORER # 왼쪽 하단에  생김
```
```py
Article.objects.create(title = "test", content = "test")
```
```py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name = 'articles'),
]
```
1) articles 페이지
```py
# apps - urls.py
path('', views.articles, name = 'articles'),

# apps - views.py

def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles, # 출력시 전체 / 입력시 부분
    }
    return render(request, "articles.html", context)


# apps - template - articles.html 파일
{% extends "base.html" %}

{% block content %}
<a href="{% url "new"%}">글쓰기</a>
    {% for article in articles %}
        <div>{{ article.id }}</div>
        <div>{{ article.title }}</div><br>
    {% endfor %}
{% endblock %}

```

2) new 페이지
```py
# apps - urls.py 파일
path('new/', views.new, name = 'new'), # 추가
path('create/', views.create, name = 'create'), # 추가

# apps - views.py 파일
from django.shortcuts import render, redirect # redirect
from .models import Article # apps 내부 model의 Article 함수

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title = title, content = content)
        return redirect("articles")
    return redirect("articles")

# apps - template - new.html 파일

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

3) article_detail 페이지
```py
# apps - urls.py
path('<int:pk>/article-detail/', views.article_detail, name ='article_detail'),

# apps - views.py
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article,
    }
    return render(request, "article_detail.html", context)

# apps - article_detail.html
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
<a href="">수정</a>

{% endblock content %}

```

4) delete 페이지
```py
# apps - urls.py
path('<int:pk>/delete/', views.delete, name = 'delete'),

# apps - views.py
def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(id=pk)
        article.delete()
        return redirect("articles")
    return redirect("articles_detail")

# apps - article_detail.html
<form action ="{% url "delete" article.pk %}" method="POST">{% csrf_token %}
<button type="submit">삭제</button>
</form>
```

3) edit 페이지
```py
# apps - urls 
path('<int:pk>/edit/', views.edit, name = 'edit'),
path('<int:pk>/update', views.update, name = 'update'),

# apps - views
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

# app - templates - edit, update.html
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
전문
```py
# 로컬 - urls
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('articles/', include("articles.urls")),
]

# apps - urls

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


# apps - views

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

### 로컬 - template - base.html
```html
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

### apps - index
```html
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

### apps - article
```html
{% extends "base.html" %}

{% block content %}
<a href="{% url "new"%}">글쓰기</a>
    {% for article in articles %}
        <div>{{ article.id }}</div>
        <div> <a href = "{% url "article_detail" article.pk %}"> {{ article.title }} </a></div><br>
    {% endfor %}
{% endblock %}
```

### apps - article_detail
```html
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

### apps new
```html
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
### apps - edit
```html
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


