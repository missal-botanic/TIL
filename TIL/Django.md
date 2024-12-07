


```bash
conda create --name jg python=3.10 # 가상환경
```
```bash
pip install django==4.2 # 장고 설치
```

```bash
django-admin startproject my_first_pjt jg

django-admin startproject my_first_pjt jg . # 바닥에 파일 생성

cd my_first_pjt 
```
```bash
python manage.py runserver
```
```
1. 앱 생성
2. 앱 등록
```

```
settings.py : 프로젝트의 설정을 관리하는 곳

urls.py : 어떤 요청을 처리할지 결정하는 곳 

__init__.py : 하나의 폴더를 하나의 파이썬 패키지로 인식하도록 하는 파일 

→ 3버전 이상으로 가면 없어도 됩니다. 하지만, 3버전 이하에서도 동작하도록 호환성을 위해 지키는 규칙입니다!

wsgi.py : 웹 서버 관련 설정 파일

manage.py : Django 프로젝트 유틸리티 (조종기)
```
```
admin.py - 관리자용 페이지 관련 설정

apps.py - 앱 관련 정보 설정

models.py - DB관련 데이터 정의 파일

tests.py - 테스트 관련 파일 

views.py - 요청을 처리하고 처리한 결과를 반환하는 파일
```
```
마지막에도 ,  Trailing commas
```
```
MTV Pattern

- Model
    - MVC에서의 Model입니다.
    - 데이터와 관련된 로직을 처리합니다.
        
        → 데이터 구조 정의, 데이터베이스 기록 관리해요.
        
- Template
    - MVC에서의 View입니다.
    - 레이아웃과 화면상의 로직을 처리
        
        →즉, UI와 레이아웃을 다루어요.
        
- View
    - MVC에서의 Controller입니다.
    - 메인 비지니스 로직을 담당합니다.
    - 클라이언트의 요청에 대해 처리를 분기하는 역할을 합니다.
        - DB도 조회하고 외부로 요청하기도 해요.
        - 응답을 만들어서 클라이언트에게 전달해요
```

```
models.py -> 데이터 베이스
views.py -> 데이터 처리 반환
```

```
model - view - controller 규칙

model 데이터와 과련된 로직
view(template) - 레이아웃과 관련된 화면
controller(view) - model과 view 연결하는 로직
```

```
model 
template
view 메인비지니스, 크라이언트 요청 처리, 분기(db 조회, 외부 요청, 응답 클라이언트 전달)
```
```
/ <--- 트래일링 슬러쉬
```
```
함수형 뷰(대부분)

클래스형 뷰(상속으로 코드를 줄일 수 있다)

HttpRequest → URLs → View→ Template → View → HttpResponse
```
```
변수 {{ 변수 }} 딕셔너리의 키값이 오고 간다. 
태그 {% tag %} 반복 또는 논리를 수행 제어 흐름 + 일부 종료 태그 존재
필터 {{ 변수|필터 }} 변수에 추가 작업 + 보여지는 모습 바꿈(ex소문자화) 60개 + 커스텀 가능
주석 {# 한 줄 주석 #}
```

```py
# 앱 생성
python manage.py startapp articles # 앱 이름 복수형 권장
```
#settings.py 파일 33줄
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles', # 추가한 내용
]
```
### urls.py
```py
# my_first_pjt/my_first_pjt/urls.py

from django.contrib import admin
from django.urls import path
from articles import views

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
    return render(request, "index.html")
```
Template
```py
def hello(request):
    context = { # 딕셔너리 형태
        "name" : "희경",
    }
    return render(request, "hello.html", context) # context 추가
```

```py
def hello(request):
    name = "희경",
    tags = ["python", "django", "html", "css"] # 변수 선언
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]

    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,
    }
    return render(request, "hello.html", context)
```

```py
    <h1>hello {{name}}</h1> # 컨텐츠 호출
    <p>첫번째 태그 {{tags.0|upper}}</p> # 딕셔너리 선택
    <p>{{books}}</p> # 전체 호출
    <li>{{books.1}}</li> 
    <li>{{books.2}}</li>
<ul> # for문
    {% for book in books %}
    <li>{{book}}</li>
    {% endfor %}
</ul>
```
```
{{ tags|join:","}}
{{ tags|length}}
{{ books.today}}
```
Template Inheritance
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
```py
{% extends 'base.html' %}

{% block content %} # 도출 시작
    <h1>hello!</h1> # 내용
{% endblock content %} # 돌출 끝
```

```
settings.py
```
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # 상위 폴더 검색 범위 추가
        'APP_DIRS': True,# 장고에게 앱 안쪽 경로 찾으라 지시
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
```

