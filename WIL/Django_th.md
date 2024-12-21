### my_first_pjt
```
1) 앱생성
2) setting 등록

3) 루트 urls 편집

4) apps urls 생성 및 편집
5) apps views 편집
6) apps template/app/app.html 폴더 생성 및 편집
```
```py
#프로젝트 폴더

settings.py # 프로젝트의 설정을 관리하는 곳

urls.py # 어떤 요청을 처리할지 결정하는 곳 

__init__.py # 하나의 폴더를 하나의 파이썬 패키지로 인식하도록 하는 파일

# 3버전 이상으로 가면 필요없음. 하지만, 3버전 이하에서도 동작하도록 호환성을 위해 지키는 규칙
# 마이그레이션의 경우 삭제 금지

wsgi.py # 웹 서버 관련 설정 파일

manage.py # Django 프로젝트 유틸리티 (조종기 역할)
```
### articles , users
```py
# 앱내 폴더
admin.py # 관리자용 페이지 관련 설정

apps.py # 앱 관련 정보 설정

models.py # DB관련 데이터 정의 파일

tests.py # 테스트 관련 파일 

views.py # 요청을 처리하고 처리한 결과를 반환하는 파일
```
### DB와 views 관계
```py
models.py # 데이터 베이스
views.py # 데이터 처리 반환
```

```py
model # 데이터와 과련된 로직
template(view) # 레이아웃과 관련된 화면
view(controller) # model과 view 연결하는 로직, 메인비지니스, 크라이언트 요청 처리, 분기(db 조회, 외부 요청, 응답 클라이언트 전달)
```
```
/ <--- 트래일링 슬러쉬
```
```py
# 함수형 뷰(대부분)

# 클래스형 뷰(상속으로 코드를 줄일 수 있다)

HttpRequest → (URLs) → View→ Template → View → HttpResponse
```

```
1. view 에서 model에 접근해 모든 아티클을 가지고 온다
2. view 에서 가져온 아티클을 template으로 넘긴다
3. tempate에서 넘어온 context를 보여준다
4. view에서 템플릿을 렌더링해서 리턴한다

model -> view -> template -> context 
```
```py
import view # view 클릭시 바로 이동
```
```py
from django import forms
from django.shortcuts import render, redirect # redirect
from .models import Article # 모델 연결
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_POST, require_http_methods
```
```py
user = form.get_user() # 다른 곳에서 써야할 때
auth_login(request, user)

-> auth_login(request, form.get_user()) # 한곳에서만 쓸 때
```
```py
# Article() 와 Article. 다르다
```

```bash
# name 의 data를 지정하지 않아서 본인 url로 보내짐
http://127.0.0.1:8000/data-throw/?message=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94#

# 프로토콜 : 약속
# request, response
# 쿼리(쿼리스트링)
# ?key=value&key2=value2 과 같은 형식
```
```py
# 오류 html 표시 내용
# views 함수에 request 누락시 
>>>
TypeError at /accounts/login/
login() takes 0 positional arguments but 1 was given

pass 만 있을시
>>>
ValueError at /accounts/login/
The view accounts.views.login didn't return an HttpResponse object. It returned None instead.
```
```django
태그 {% tag %} # 반복 또는 논리를 수행 제어 흐름 + 일부 종료 태그 존재
{% extends "base.html" %}
{% block content %}

{% csrf_token %}
{% for article in articles %}
{% url "accounts:login" %}
{% if request.user.is_authenticated %}

변수 {{ 변수 }} # 딕셔너리의 키값이 오고 간다. /변수/장고폼/
{{ form.as_p }}
{{article.id}}
{{ request.user.username }}

필터 {{ 변수|필터 }} # 변수에 추가 작업 + 보여지는 모습 바꿈(ex소문자화) 60개 + 커스텀 가능

주석 {# 한 줄 주석 #}

<str:username>
<username>
```
```py
# 01
<form action="{% url 'create' %}" method="GET"> #틀림
{% csrf_token %} # 주소로 오는거 막기
# 02
if request.method == "POST":

# 03
@require_POST
@require_http_methods(["GET", "POST"])
```
```py
# 산
return render(request, "hello.html", context)
{% url 'update' article.pk %}
```
### urls.py
```py
path("articles/", include("articles.urls"))
```
### views.py
```py
from django.http import HttpResponse

# HttpResponse
def index(request): 
	response = HttpResponse("<h1>Hello, Django!</h1>") # html바로 코딩 + 라이브러리 로딩 필요
	return response
```
```py
# html render
from django.shortcuts import render

def index(request):
    return render(request, "index.html") # 기본 코드
```

```py
# 기초 딕셔너리
def hello(request):
    context = { # 딕셔너리 형태
        "name" : "희경",
    }
    return render(request, "hello.html", context) # context 추가
```
```py
# 복합 딕셔너리
def hello(request):
    name = "희경",
    tags = ["python", "django", "html", "css"] # 변수 선언
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]

    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,
    }
    return render(request, "hello.html", context) # context 추가
```
### templates HTML
```django
<h1>hello {{name}}</h1> # 컨텐츠 호출

<p>첫번째 태그 {{tags.0|upper}}</p> # 딕셔너리 선택
<p>{{books}}</p> # 전체 호출
<li>{{books.1}}</li> 
<li>{{books.2}}</li> # 부분 호출

<ul> # for문 연속 출력
    {% for book in books %}
    <li>{{book}}</li>
    {% endfor %}
</ul>
```
### tag 예시
```django
{{ tags|join:","}}
{{ tags|length}}
{{ books.today}}
```


### HTML type 과 id
```html
<form action="#" method="#"> <!-- action 데이터 전송 될 url  method GET, POST 방식-->
    <label for = "my-data">데이터 입력 : </label>
    <input type = "text" id = "my-data" > <!-- for과 id 일치 -->
    <button type = "submit">전송</button>
```
### HTML name
```html
<form action="#" method="#"> 
    <label for = "message">데이터 입력 : </label>
    <input type = "text" id = "message" name="message"> <!--  대다수 모두 일치 시킨다 -->
    <button type = "submit">전송</button>
```
```html
<!-- 01 -->
<form action="http://127.0.0.1:8000/data-catch/" method="GET">
<!-- 02 -->
<form action="/data-catch/" method="GET">
<!-- 03 -->
<form action="{% url 'articles' %}" method="GET">
<form action="{% url 'articles:articles' %}" method="GET">
<!-- 04 -->
<form action="" method="GET">
?next=/ 조합
```


```py
# 입력페이지 전문
{% extends 'base.html' %}

{% block content %}
<h1>hello</h1>

<form action="/data-catch/" method="GET">
    <label for = "message">데이터 입력 : </label>
    <input type = "text" id = "message" name="message">

    <button type = "submit">전송</button>
{% endblock content %}

>>>
http://127.0.0.1:8000/data-catch/?message=asaas 
# view 와 입력 페이지에서 수정하지 않으면 catch url 에서 머무름
```

### view
```py
def data_catch(request):
    message = request.GET.get("message") # "message" (html name 입력 부분)
    context = {"message" : message} # 변수
    return render(request, "data_catch.html", context) # 마지막 context 추가
```
```py
변수.get("message") # 파이썬 문법
변수.get("message", 2) # 없을시 2를 반환
```
```django
# 출력 페이지
<h1>Data Catch</h1>
<h3>Current Data</h3>
<p>Curent data is : {{ message }} </p> 
<!-- "message" (view의 context{} 부분) -->
```

### request, request 출력확인
```py
print(request) 
>>>
<WSGIRequest: GET '/data-catch/?message=sacs'> 

print(request.GET) 
>>>
<QueryDict: {'message': ['sacs']}> #  QuertDict 타입 장고의 class
```
----
```py
dispatcher # 데이터를 목적지로 보내는 주체
URL # 들어온 요청을 어디로 보내서 처리할지 결정하는것
```
```py
트레일링 슬래시 # URL 뒤에 붙는 슬래시
www.web.com # 파일
www.web.com/ # 디렉토리

# 원래 url은 path 가 반듯이 있어야 하지만 자동으로 / 붙이고, 자동 index.html 파일 찾음
```
### Variable Routing

```py
users/<username>/ # 미입력시 str
users/<str:username>/ # 문자열
users/<int:username>/ # 0또는 양의 정수
```
```py
# urls.py
path('users/<username>/', views.profile) # <인수> URL에서 'username' 인수를 받겠다 정의

# views.py
def profile(request, username):  # url 의 /'username' 내용 받는 인수
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context) # context 반환 
```
### urls 
```py
# 통째로 혹은 일부

from .models import Article # .은 현재 파일과 동일한 디렉토리에 있는 models.py 파일에서 Article 클래스
from .forms import ArticleForm # .은 현재 디렉토리 내의 forms.py 파일 그 파일에서 ArticleForm을 가져오는 코드
from . import views # . 현재 디렉토리 내의 views.py 파일을 통째로
```

### app urls
```py
urlpatterns = [
    path('users/<str:username>/', views.profile) # 이전버전
    path('<str:username>/', views.profile), # 수정 후 
     
    path('users/',  views.users), #이전버전
    path('',  views.users), # 수정 후
]
```
```py
# name="data-throw" 주소 네임화

# urls
path("data-catch/", views.data_catch, name="data-catch"), # name="data-catch" 추가 (루트 name화)

# HTMl
<form action="/articles/data-catch/" method="GET"> # 수정 전

<form action="{% url 'data-catch' %}" method="GET"> # 수정 후 
```

# Template Inheritance
### template 상속
### base.html
```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% block content %} # 틈 시작 
    {% endblock content %} # 틈 끝
</body>
</html>
```
### 상속 받는 HTML
```django
{% extends 'base.html' %}

{% block content %} # 도출 시작
    <h1>hello!</h1> # 내용
{% endblock content %} # 돌출 끝
```
### include()
```py
# 01 urls
from django.contrib import admin
from django.urls import path, include # 추가
from articles import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 파일.함수
    path('articles/', include("articles.urls")), # include() + 폴더.파일
    path('user/', include("users.urls"))
]
```
## models 마이그레이션
```py
데이터 # 데이터가 모인 곳
쿼리 # 조작 언어
스키마 # 관계의 정의

1. 테이블
3. Priamay key = 테이블 인덱스 # 장고는 자동 생성
4. 행
5. 열
```

```py
Queryset == ORM를 사용해서 # 데이터베이스로 부터 전달 받은 객체

objects # manage의 기본 이름

# MyModel.objects.all()
```

**CRUD** Create Read Updata Delete 
### shell 명령어 모음
```bash
Create
# shell에서 사용

article = Article() # 클래스로 객체 생성
article.title = 'first_title'  # 생성된 객체의 title 필드에 'first_title'을 할당
article.content = 'my_content' # 생성된 객체의 content 필드에 'my_content'를 할당

article = Article.objects.get(id=pk)

# 여기에서 전체 Article을 조회해보면
Article.objects.all() # 비어있다
>>>
<QuerySet []>
# save()하기전에는 저장되지 않음
article.save()

article = Article(title='두번째 제목', content='두번째 내용')

# save()가 필요하지 않는 방법
Article.objects.create(title='third title', content='마지막 방법')

Read
# 다시 전체 Article을 조회해보면 하나의 article 확인 가능
Article.objects.all()
>>>
<QuerySet [<Article: Article object (1)>]> # 1은 객체의 ID

Article.objects.get(id=2) # 하나만 조회 없을시, 여러개일 시 멈춤
>>>
<Article: 두번째 제목> # 오브젝트를 바로 가지고옴

Article.objects.filter(content='my_content') # 여러개 리턴 look up
Article.objects.filter(id__gt=2) # 2보다 큰 id
Article.objects.filter(id__in=[1,2,3]) # 1,2,3에 속하는 id
Article.objects.filter(content__contains='my') # content에 'my'가 포함된
...

# 속성 하나씩 접근하기

article.title # 제목 

article.content # 내용

article.create_at # 생성일시

article.id # pk(id)

.all() # 조회시 내용 추가
```

```py
# 수정

article = Article.objects.get(id=1) # 실제 데이터를 수정하기 위해 변수에 연결시키는 작업
article.title = 'updated title'
article.save()

first_article = Article.objects.get(id=1) # 실제 데이터를 수정하기 위해 변수에 연결시키는 작업
first_article.content = "안녕하세요"
first_article.save()
new_article = Article.objects.get(id=1) # 실제 데이터를 수정하기 위해 변수에 연결시키는 작업
new_article.content
>>> 
'안녕하세요'

first_article.content
>>>
'안녕하세요'

```
```py
# 삭제

article = Article.objects.get(id=2)
article.delete()
>>>
(1, {'articles.Article': 1})
```
```py
# model 파일 출력 추가

class Article(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 추가된 내용/ 출력 확인 용(선택)
        return self.title

>>>
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]> # 전 
<QuerySet [<Article: 첫번째 제목>, <Article: 두번째 제목>, <Article: 세번째 내용>]> # 후
```
template 파일

```html
<form action="" method="GET">  <!-- db 사용시 -->
# 입력 내용들
</form>
```
```py
# id = pk 같은 효과
{{article.id}} 
{{article.pk}}
article = Article.objects.get(id=pk)
```

```py
# get 방식은 DB에 영향을 주지 않는것

# POST 와 GET 차이
# GET 은 data 를 url로 보낸다
# POST 는 body에 담아 보낸다

# views
def create(request):
    title = request.POST.get("title") # 2) POST
    content = request.POST.get("content")

# template
<form action="{% url 'create' %}" method="POST"> # 1) POST 
    {% csrf_token %} # csrf token 3) 추가

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
```py
return redirect("articles") # 바른 연결
return redirect("articles.html") # 틀린방식
```
```py
<a href="{% url "delete" article.pk %}">삭제</a> # <a> 태그는 기본적으로 GET 요청을 보내는 링크
<form action ="{% url "delete" article.pk %}" method="POST">{% csrf_token %} 삭제</form> # <form> 태그는 POST 요청을 보내는 방법
```


## C
```py
# views

def new(request): # 화면 연출 효과만 존재
    return render(request, "new.html")

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 새로운 article 저장
    Article.objects.create(title=title, content=content)
    return render(request, "create.html") # 리턴 내용 없음

# html

<form action="{% url 'create' %}" method="GET"> # 바람직하지 못한 GET 하지만 view에서 대비가 없다면 작동
    <label for="title">제목</label>
    <input type="text" name="title" id="title"><br><br>

    <label for="content">내용</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br><br>

    <button type="submit">저장</button>
</form>


```

```py
redirect

# view
from django.shortcuts import render, redirect # 추가

return render(request, "articles.html") # 전 페이지 creat는 Template action POST 위치와 연결되어 있음?

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return render(request, "create.html") # 전

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles") # 후

# create.html 삭제
```
## R
```py
게시판 기본 형태

# view
from .models import Article # 모델 연결

def articles(request): # 처음 페이지 로딩시
    articles = Article.objects.all().order_by("-created_at")  # (복수형) 모든데이터 호출 제목, 내용, 수정날짜.... / .order_by("-created_at") 역순 정렬 .order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)

# html
{% for article in articles %}
    <li>
        <div>번호 : {{ articles.id }}</div>
        <div>제목 : {{ articles.title }}</div>
        <div>내용 : {{ articles.content}}</div>
        <br>
    </li>
{% endfor %}
```
### article detail
```py
# urls
path("<int:pk>/", views.article_detail, name="article_detail")

# views
def article_detail(request, pk):
    article = Article.objects.get(id=pk) # s가 아님
    context = {
        "article": article,
    }
    return render(request, "article_detail.html", context)

# html

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
path("delete/", views.delete, name="delete"), # 1) 잘못됨
path("<int:pk>/delete/", views.delete, name="delete"), # 1) id 필요

Article.objects.delete(id=pk) # 2) 잘못됨
article = Article.objects.get(id=pk) # 2) 호출 후 개별 진행 필요
article.delete()
```
```html
<input ...  value="{{ article.title }}"/> <!-- value 값에 -->
<textarea ...> <!-- value 값 없이 <>안에<> -->
```

```py
# 수정하기

# articles - urls
path("<int:pk>/edit/", views.edit, name="edit"),
path("<int:pk>/update/", views.update, name="update"),

# views
def update(request, pk):
  article = Article.objects.get(id=pk)
  article.title = request.POST.get("title")
  article.content = request.POST.get("content")
  article.save()
  return redirect("article_detail", article.pk)


def update(request, pk): # POST 구분
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.get(id = pk)
        article = Article.objects.create(title = title, content = content)
        return redirect("article_detail", article.pk) # request 없음
    return redirect("article_detail", article.pk)

# html
  <form action="{% url 'update' article.pk %}" method="POST">  # update 변경
    {% csrf_token %}
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text" id="inputGroup-sizing-sm">Small</span>
      <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" name="title" value="{{ article.title }}"/> # value="{{ article.title }}"
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text">With textarea</span>
      <textarea class="form-control" aria-label="With textarea2" name="content">{{ article.content }}</textarea> # > {{ article.content }} <
    </div>
    <button type="submit" class="btn btn-primary">수정</button> # 텍스트 수정으로 변경
  </form>

  <a href = {% url "article_detail" article.pk %}>뒤로</a>
```
### 로그인

```
index 의 articles:hello 의 articles는 
urls.py에서 정의된 네임스페이스

views에서는 모든 폴더를 찾는다. 
```
```
auth (인증, 권한)

비연결 지향, 한번 통신하고 끝
무상태, 서로를 잊어버림 + 독립적 메세지

>>> 매번 로그인하고 작업해야한다.

쿠키 = 항상 같이 보내는 자료(유저의 로컬에 저장, 변경 가능)

섹션 = 로그인 하면 그 쿠키에 서버가 로그인 넘버를 넣어서 클라이언트에게 전달
클라이언트가 서버에 쿠키를 통해 임의의 난수(세션 id)전달 

세션쿠기 : 브라우저가 닫히면 쿠키 삭제
지속쿠키 : 하드디스크에 저장됨 ( MAX_Age 지정하면 삭제가능 )
```
```
로그인 - Session을 Create함
장고 기본적인 Model user table 가지고 있음, 필요하면 확장
```
```py
# 로그아웃은 세션을 지우는것
```
```django
 <!-- base.html -->
<div class="navbar">
    <a href="{% url "accounts:login" %}">로그인</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="로그아웃"></input>
    </form> # 이부분 누락시 로그인시 로그인 세션 형성이 안됨
</div>
```
```
200 성공
400 클라이언트 실패
500 서버에서 실패
get(주소창으로 명령어 날리는거 )-> 방어 -> 405 오류유도
```

```django
모든 template에서 항상 접근 가능한 context가 있다.
request.user에서의 auth.User 혹은 AnonymousUser 인스턴스
{% if request.user.is_authenticated %}
{{ request.user.username }}
```
```py
# 로그인 후 다음에 들어갈 주소
?next=/
```

```
null = True # DB에 null 을 저장해도 된다
null은 정의되지 않는값, 빈값이 아니다.
텍스트 필드에 db에 ""와 null이 혼동 될 수 있다. 
```
```py
# 클래스 확인하기 
form - ModelForm - BaseModelForm
class BaseModelForm(BaseForm):
    instance: Any = ...
    def __init__(
        self,
        data: Mapping[str, Any] | None = ..., # request.POST 부분
        files: Mapping[str, File] | None = ..., # 파일 부분
        auto_id: bool | str = ...,
        ...
```
```
python manage.py runserver # 개발용 임시 환경
동시 20~25명 정도면 터짐`
```
```
<img src="{% static "articles/image.png" %}" alt="image"> # 이미지 실패 했을 때
```
배포시
```bash
collectstatic # 마지막 배포시 한곳에 모음
python manage.py collectstatic
```
```py
DEBUG = True # True 경우 STATIC_ROOT가 작동하지 않는다.
```
```py
# 통합 전 코드
filse = request.FILES
form = ArticleForm(request.POST, filse)
# 통합 후 코드
form = ArticleForm(request.POST, request.FILES) # 추가
```
```py

input_image = request.FILES["image"]
article.image = input_image
article.save() # views 장고 폼을 쓰지 않을 경우

<input type="file" name="image"> # html장고폼을 쓰지 않을 경우

```
```bash
python manage.py makemigrations  # 생성
python manage.py migrate  # 반영

```
```
print(pk)
>>> 40
숫자만 출력
```
```
**objects**는 **매니저(Manager)**의 이름으로, Django 모델의 쿼리 인터페이스를 제공하는 역할을 하며, 복수 형태로 사용되는 이유는 여러 객체에 대한 쿼리 작업을 처리하기 위해서입니다.
**get_object_or_404**는 단일 객체를 반환하는 헬퍼 함수로, object라는 단수형을 사용합니다.
```
```bash
<int:comment-pk> # 터짐
<int:comment_pk> # 정상 작동
```
settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_# def
```py
요청(Request)

- Start Line
    - Method, Traget, HTTP Version
- Headers
    - 요청에 필요한 여러가지 메타 정보
- Body
    - 요청에 필요한 여러가지 데이터

응답(Response)

- Start Line
    - HTTP Version,  Status Code, Status Message
- Headers
    - 응답에 대한 열가지 메타 정보
- Body
    - 요청을 처리한 여러가지 데이터 # 장고 기초에서는 html이 응답
```

```py
'POST' '/articles/' #새로운 article 생성

'GET' '/articles/' # 목록 조회

'GET' '/articles/1' # 1번 article 조회

'DELETE' '/articles/1/' #1번 article 삭제

'PATCH'  # 일부 수정

→ 'POST' '/articles/create/' (X)

→ 'POST' '/articles/' (O)
```
```py
1. url(로컬)
2. url(앱) # 비어 있더라도 만들어야함
3. model
```

JSON
```py
'.json' # 형식으로 사용
문자는 '"'으로 묶여야하며  # 사용 '' 사용 x 
'true' 'false' , #True 사용 x

[json]: 순서보장
{josn}: 순서 x
```
name="articles")

기본값 : user.article_set.all
```py
AUTH_USER_MODEL = 'accounts.User' # Django에서 기본 사용자 모델 대신 accounts 앱에 정의된 User 모델을 사용하도록 설정하는 코드
```
```
STATICFILES_DIRS = [
    BASE_DIR / "static",  # 첫 번째 디렉터리
    BASE_DIR / "assets",  # 두 번째 디렉터리
]
```
```py
 /~/ # 사용자의 홈 디렉터리에서 시작하는 절대 경로
 ~/ # 경로 구분자로 사용되며, 상대 경로나 절대 경로
 ```
 ```
 Django에서 settings.AUTH_USER_MODEL은 settings.py에서 정의된 사용자 모델을 참조하는 방식입니다. 이는 사용자가 커스텀 사용자 모델을 설정한 경우 유용합니다. 반면 get_user_model은 현재 프로젝트에서 실제로 사용되는 사용자 모델을 동적으로 반환하는 함수입니다. 
 ```
 ```py

@login_required # next 존재 미처리시 오류
@require_POST
def like(request, pk):


@require_POST
def like(request, pk):
    if request.uesr.is_authenticated: # 함수 진행 정지로 오류 없음

```
```
# 같다
if:
else:
 return

if
return
```

```py
1. url(로컬)
2. url(앱) # 비어 있더라도 만들어야함
3. model
```
{% for article in articles %} # article 새 변수


json_data = serializer.data # 속성접근 
json_data = serializer.data # 함수호출


```bash
# 방법01
article = Article()
article.title = 'first_title' 
article.content = 'my_content'
article.save() # save()하기전에는 저장되지 않음

# 방법02
article = Article(title='두번째 제목', content='두번째 내용')
article.save()


# 방법03
Article.objects.create(title='third title', content='세번째 내용') 
``
```py
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title = title, content = content)
        return redirect("articles")
    return redirect("articles")
```
```py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect("article_detail", article.pk)
    return redirect("new")
```
```html
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
```
```py
<input type='text' id='title' name='title' value = "{{article.title}}"><br> # 전

{{ form.as_p }} # 후
```