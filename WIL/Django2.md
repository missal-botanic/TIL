```py
apps - forms.py 생성
```
```py
# apps - forms.py
from django import forms

class ArticleForm(forms.Form):
    GENRE_CHOICES = [
        ("techology", "Techology"),
        ("life", "Life"),
        ("hobby", "Hobby")
    ]
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    #genre = forms.ChoiceField(choices=GENRE_CHOICES)

# apps - html
{% extends 'base.html' %}

{% block content %}
  <form action="{% url 'create' %}" method="POST"> <!-- views.create로 보냄 -->
    {% csrf_token %}
    {{ forms.as_p}}
    <button type="submit" class="btn btn-primary">Primary</button>
  </form>

  <a href = {% url 'articles' %}>뒤로</a>
{% endblock %}
```

```py
# apps - views.py
def create(request):
    form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
    if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
        article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
        return redirect("article_detail", article.pk)
    return redirect("new")
```

new +> create # 통합 + 이름변경

```py
# apps - forms.py
from django import forms

from articles.models import Article

class ArticleForm(forms.ModelForm): # 이름 변경가능
    class Meta: # 이름 변경 불가능
        model = Article
        fields = "__all__"
        #fields = ["title", "content"]
        #exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요
```

```py
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
        if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
            article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "create.html", context)
```



edit - update

```py
#instance 가 없으면 생성
#instance = article 있으면 수정

def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {"form":form, "article" : article}
    return render(request, "update.html", context)
```
URL namespace
```py

# 같은 urls 경우 setting기준으로 제공
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'articles',
    'users',
]

# apps - urls 추가
app_name = "articles" # namespace

# apps - html 변경
<form action="{% url 'create' %}" method="POST">
<form action="{% url 'articles:create' %}" method="POST">

# apps - views - redirect 변경
return redirect("article_detail", article.pk)
return redirect("articles:article_detail", article.pk)

```
Template Namespace
```py
# apps - templates 폴더에 article 폴더 추가
templates/articles

# apps - view - return render() 변경
return render(request, "profile.html", context)
return render(request, "articles/profile.html", context)

```
index 의 articles:hello 의 articles는 urls -> views를 의미한다. views에서는 모든 폴더를 찾는다. 
```
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
```bash
python manage.py createsuperuser
admin / adim1234
admin@test.com
```


```py
# 01차
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)

# 02차
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
        
    else:
        form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)
---

{% extends "base.html" %}

{% block content  %}
<h1>login</h1>
<form action = "{% url "accounts:login" %}" method = "POST">
{% csrf_token %}
{{form.as_p}}

<button type = "submit">login</button>

</form>

{% endblock content %}
```
로그아웃
```

path('logout/', views.logout, name='logout'),

def logout(request):
    auth_logout(request)
    return redirect("index")

    
<div class="navbar">
    <a href="{% url "accounts:login" %}">로그인</a>
</div>
<form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="로그아웃">
</form>
```

```py
일반적
try:
    article = Article.objects.get(id=pk)
except Article.DoesNotExist:
    return redirect("articles:articles")
장고적

from django.shortcuts import render, redirect, get_object_or_404

def article_detail(request, pk):
    #article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/article_detail.html", context)
```
```py
from django.views.decorators.http import require_POST

@require_POST
def logout(request):
    auth_logout(request)
    return redirect("index")

#
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET", "POST"]) # 두가지 외에 차단
def login(request): # 두가지중 분기점 필요
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)



@require_http_methods(["GET", "POST"]) 
def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect("index")
    return render(request, "accounts/login.html", {"form": form})


{% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">글쓰기</a>
{% else %}
    <a href="{% url "accounts:login" %}">로인그하고 작성하기</a>
{% endif %}

```

```py
#

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("index")

#
{% if request.user.is_authenticated %}
<h3>{{ request.user.username }}안녕하세요.</h3>
<form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="로그아웃">
</form>

{% else %}
<div class="navbar">
    <a href="{% url "accounts:login" %}">로그인</a>
</div>
```

```py
 from django.contrib.auth.decorators import login_required   
# b
if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    return redirect("index")
# a
if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    next_url = request.GET.get("next") or "index" # 추가
    return redirect(next_url) # 추가


<h1>login</h1>
<form action = "" method = "POST"> # action 지워서 마지막 위치로 복귀
{% csrf_token %}
{{form.as_p}}
<button type = "submit">login</button>
</form>