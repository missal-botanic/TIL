### 준비
```bash
conda create --name jg python=3.10 # 가상환경
```
### 설치
```bash
pip install django==4.2 # 장고 설치
```
```bash
django-admin startproject my_first_pjt jg # 프로젝트 시작

django-admin startproject my_first_pjt jg . # 바닥에 파일 생성

cd my_first_pjt # 생성한 프로젝트 폴더로 이동
```
### 실행
```bash
python manage.py runserver # 서버 실행
```
### 앱 생성
```py
# 1. 앱 생성 Bash
python manage.py startapp articles # 앱 (이름 복수형 권장)
python manage.py startapp users

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

 마지막에 "," Trailing commas
```
### my_first_pjt
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
```py
태그 {% tag %} # 반복 또는 논리를 수행 제어 흐름 + 일부 종료 태그 존재

변수 {{ 변수 }} # 딕셔너리의 키값이 오고 간다. 
필터 {{ 변수|필터 }} # 변수에 추가 작업 + 보여지는 모습 바꿈(ex소문자화) 60개 + 커스텀 가능

주석 {# 한 줄 주석 #}
```
### urls.
```py
import view # view 클릭시 바로 이동
```
```py
# my_first_pjt/my_first_pjt/urls.py

from django.contrib import admin
from django.urls import path
from articles import views # from(폴더),import(파일)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index), # 추가한 내용
]
```
### views.py
```py
from django.http import HttpResponse

def index(request): # 추가 함수 
	response = HttpResponse("<h1>Hello, Django!</h1>") 
	return response
```
### html 뷰
```py
# my_first_pjt/articles/views.py
from django.shortcuts import render

def index(request):
    return render(request, "index.html") # 기본 코드
```
### Template
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
### HTML
```py
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
```
{{ tags|join:","}}
{{ tags|length}}
{{ books.today}}
```
# Template Inheritance
### base
```py
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
```py
{% extends 'base.html' %}

{% block content %} # 도출 시작
    <h1>hello!</h1> # 내용
{% endblock content %} # 돌출 끝
```
```py
# settings.py
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
    return render(request, "data_catch.html", context)# 마지막 context 추가
```
```py
# 출력 페이지
<h1>Data Catch</h1>
<h3>Current Data</h3>
<p>Curent data is : {{ message }} </p> # "message" (view의 context 부분)
```
```py
변수.get("message") # 파이썬 문법
변수.get("message", 2) # 없을시 2를 반환
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
# urls.py
path('users/<username>/', views.profile) # <인수> URL에서 'username' 인수를 받겠다 정의

# views.py
def profile(request, username):  # url 의 /'username' 내용 받는 인수
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context) # context 반환 
```

```py
users/<username>/ # 미입력시 str
users/<str:username>/ # 문자열
users/<int:username>/ # 0또는 양의 정수
```


```py
# 01 urls
from django.contrib import admin
from django.urls import path, include
from articles import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 파일.함수
    path('articles/', include("articles.urls")), # include() + 폴더.파일
    path('user/', include("users.urls"))
]

# 02 urls
from django.urls import path
from . import views # . 같은 폴더에 위치

# app urls
urlpatterns = [
    path('users/<str:username>/', views.profile) # 이전버전
    path('<str:username>/', views.profile), # 수정 후 
     
    path('users/',  views.users), #이전버전
    path('',  views.users), # 수정 후
]
```
```py
urlpatterns = [
    path('data-throw/', views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"), # name="data-catch" 추가 (루트 name화)
]

# HTMl
<form action="
/articles/data-catch/" method="GET"> # html 파일 수정 전

<form action="{% url 'data-catch' %}" method="GET"> # html 파일 수정 후 
```
### models 마이그레이션
```py
데이터 # 데이터가 모인 곳
쿼리 #조작 언어
스키마 #관계의 정의#

1. 테이블
3. Priamay key = 테이블 인덱스 # 장고는 자동 생성
4. 행
5. 열
```
```bash
# 마이그레이션 : 파이썬 모델을 DB에 생성 준비
python manage.py makemigrations  # 생성
```
```bash
# 마이그레이션 : 파이썬 모델을 DB에 반영
python manage.py migrate  # 반영

# 새로운 열 생성시 빈공간 채우는 메시지 -> 1선택 -> 그냥 엔터 -> 자동 채움
# 마이그레션 파일 지울 경우 `__init__.py` 파일은 삭제하지 않도록 주의
```
``` bash
sqlite # 익스텐션 설치

python manage.py migrate # 동기화 + 최초 한번은 마이그레이션 필요

control + shift + p -> sqlite 검색->sqlite OPEN DATABASE -> db.sqlite3 # 선택

SQLITE EXPLORER # 왼쪽 하단에  생김

```