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

```py

# 최상위폴더(manage.py와 같은 위치로 이동)
python manage.py startapp articles # 앱 (이름 복수형 권장)
python manage.py startapp users

mkdir apps/articles # app 파일 위치 변경시
python manage.py startapp articles apps/articles

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
from django.urls import path
from articles import views # from(폴더),import(파일) % 삭제 예정 %
from . import views # index용 ??? 확인 필요 삭제 필요

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name='index'), # 추가 views, index 위치는 app 아래에
    #path("users/<str:username>/, views.users, name='users')
    path("articles/", include("articles.urls"))
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

## R
```py
# view
from .models import Article # 모델 연결

def articles(request): # 처음 페이지 로딩시
    articles = Article.objects.all().order_by("-created_at")  # 모든데이터 호출 제목, 내용, 수정날짜.... / .order_by("-created_at") 역순 정렬 .order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)

# template
{% for article in articles %}
    <li>
        <div>번호 : {{ article.id }}</div>
        <div>제목 : {{ article.title }}</div>
        <div>내용 : {{ article.content}}</div>
        <br>
    </li>
{% endfor %}

```
## C
```py
# template 파일

<form action="" method="GET"> # form으로 묶음
# 입력 내용들
</form>

<form action="{% url 'create' %}" method="GET"> # 바람직하지 못한 GET 하지만 작동
    <label for="title">제목</label>
    <input type="text" name="title" id="title"><br><br>

    <label for="content">내용</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br><br>

    <button type="submit">저장</button>
</form>

# views 파일
def new(request):# 화면 연출 효과만 존재
    return render(request, "new.html")

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 새로운 article 저장
    Article.objects.create(title=title, content=content)
    return render(request, "create.html") # 리턴 내용 없음
```
```py
# id = pk
{{article.id}}
{{article.pk}}
```
```py
# get 방식은 DB에 영향을 주지 않는것

# 서버에서 유저 기억하는 방식 세션

POST 와 GET 차이

# template 파일
<form action="{% url 'create' %}" method="POST"> # 1) POST 
    {% csrf_token %} # csrf token 3) 추가

# views 파일
def create(request):
    title = request.POST.get("title") # 2) POST
    content = request.POST.get("content")
```

```py
# settings
request와 respone 두번 반복
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # csrf 미드웨어
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

```
GET 은 data 를 url로 보낸다
POST 는 body에 담아 보낸다
```
```py
# view file
from django.shortcuts import render, redirect # redirect

return render(request, "articles.html") # 전 페이지 creat는 Template action POST 위치와 연결되어 있음?

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    # 새로운 article 저장
    Article.objects.create(title=title, content=content)
    return render(request, "create.html") # 전

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles") # 후

# create.html 삭제
```
```py
# articles - urls 파일
path("<int:pk>/", views.article_detail, name="article_detail")

# articles - views 파일
def article_detail(request, pk):
    article = Article.objects.get(id=pk) # s가 아님
    context = {
        "article": article,
    }
    return render(request, "article_detail.html", context)

# articles - template 파일

<h2>article detail</h2>

<h3> {{ article.title }} </h3>
<p> {{ article.content }} </p>
<p> {{ article.created_at}} </p>
```


NoReverseMatch at
```py
# articles - views 파일
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("article_detail") # 오류 발생

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article.objects.create(title=title, content=content) # 실행 + 변수 지정
    return redirect("article_detail", article.pk)  # 실행된 내용이 담긴 변수에서 pk 사용
```
```py
path("delete/", views.delete, name="delete"), # 잘못됨
path("<int:pk>/delete/", views.delete, name="delete"),

Article.objects.delete(id=pk) # 잘못됨
article = Article.objects.get(id=pk)
article.delete()

<a href="{% url 'delete' %}">지우기</a> # 잘못됨
<form action="{% url 'delete' article.pk %}" method = "POST" >
    {% csrf_token %}
    <input type='submit' value='삭제'>
</form>
```
```py
<input ...  value="{{ article.title }}"/> # value 값에
<textarea ...> # value 값 없음,
```

```py
# articles - urls 파일
path("<int:pk>/edit/", views.edit, name="edit"),
path("<int:pk>/update/", views.update, name="update"),

# articles - views 파일
def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get("title")
  article.content = request.POST.get("content")
  article.save()
  return redirect("article_detail", article.pk)


def update(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.get(id = pk)
        article = Article.objects.create(title = title, content = content)
        return redirect("article_detail", article.pk) # request 없음
    return redirect("article_detail", article.pk)

# article -templates 파일
  <form action="{% url 'update' article.pk %}" method="POST">  # update 변경
    {% csrf_token %}
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text" id="inputGroup-sizing-sm">Small</span>
      <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" name="title" value="{{ article.title }}"/> # value="{{ article.title }}"
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text">With textarea</span>
      <textarea class="form-control" aria-label="With textarea2" name="content">{{ article.content }}</textarea> # {{ article.content }}
    </div>
    <button type="submit" class="btn btn-primary">수정</button> # 텍스트 변경
  </form>

  <a href = {% url "article_detail" article.pk %}>뒤로</a>
```