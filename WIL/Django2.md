### djang.forms
```py
apps - forms.py 생성
```
```py
# forms
from django import forms # 추가

class ArticleForm(forms.Form):
    GENRE_CHOICES = [
        ("techology", "Techology"),
        ("life", "Life"),
        ("hobby", "Hobby")
    ]
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    genre = forms.ChoiceField(choices=GENRE_CHOICES) # 드롭다운 예시

# views
def create(request):
    form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
    if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
        article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
        return redirect("article_detail", article.pk)
    return redirect("new")

# html
<form action="{% url 'create' %}" method="POST"> <!-- views.create로 보냄 -->
    {% csrf_token %}
    {{ forms.as_p}} # 추가
    <button type="submit" class="btn btn-primary">제출</button>
</form>
  <a href = {% url 'articles' %}>뒤로</a>
```

new +> create 통합, 이름변경

```py
# forms
from django import forms
from articles.models import Article # 모델 호출

class ArticleForm(forms.ModelForm): # 이름 변경가능
    class Meta: # 이름 변경 불가능
        model = Article
        fields = "__all__" # or fields = ["title", "content"]
        exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요

# views
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

edit - update 통합, 이름변경

```py
#instance 가 없으면 생성
#instance = article 있으면 수정

def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article) # POST 수정 사항 반영 용도, 해당 인스턴스를 지정하는것 id 역할
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article) # GET 처음 사이트 보여줄 때 용도
    
    context = {"form":form, "article" : article}
    return render(request, "update.html", context)

# html
<input type='text' id='title' name='title' value = "{{article.title}}"><br> # 전

{{ form.as_p }} # 후

```
## URL namespace
```py

# 같은 urls 경우 setting기준으로 순서 제공
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

# apps - urls 상단에 추가
app_name = "articles" # namespace

# apps - html 변경
<form action="{% url 'create' %}" method="POST"> # 전
<form action="{% url 'articles:create' %}" method="POST"> # 후

# apps - views - redirect 변경
return redirect("article_detail", article.pk) # 전
return redirect("articles:article_detail", article.pk) # 후

```
### Template Namespace
```py
# apps - templates 폴더에 article 폴더 추가
templates/articles

# apps - view - return render() 변경
return render(request, "profile.html", context) # 전
return render(request, "articles/profile.html", context) # 후

```

```bash
python manage.py createsuperuser
admin / adim1234
admin@test.com
```


```py
# views
# 1차 로그인 화면만 구성
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)

# 02차 실제 작동하게 구성
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # 단축 가능
            return redirect("index")
        
    else:
        form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)

# html

<h1>login</h1>
<form action = "{% url "accounts:login" %}" method = "POST">
    {% csrf_token %}
    {{form.as_p}}

    <button type = "submit">login</button>
</form>

```
### 로그아웃
```py
# urls
path('logout/', views.logout, name='logout'),

# views
def logout(request):
    auth_logout(request)
    return redirect("index")

# html
<div class="navbar">
    <a href="{% url "accounts:login" %}">로그인</a>
</div>
<form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="로그아웃">
</form>
```
### 오류 처리
```py
# pythonic
try:
    article = Article.objects.get(id=pk)
except Article.DoesNotExist:
    return redirect("articles:articles")

#django way
from django.shortcuts import render, redirect, get_object_or_404

def article_detail(request, pk):
    #article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk) # 변경
    context = {
        "article": article,
    }
    return render(request, "articles/article_detail.html", context)
```
@require_POST 처리
```py
# views
from django.views.decorators.http import require_POST

@require_POST # POST 만 받는 경우, html 존재 하지 않는 경우, 분기점 필요 없음
def logout(request):
    auth_logout(request)
    return redirect("index")


from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET", "POST"]) # 두가지 외에 차단
def login(request): # 두가지중 분기점은 필요
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


# 줄이는 방법 참고용
@require_http_methods(["GET", "POST"]) 
def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect("index")
    return render(request, "accounts/login.html", {"form": form})

# html
{% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">글쓰기</a>
{% else %}
    <a href="{% url "accounts:login" %}">로인그하고 작성하기</a>
{% endif %}

```

```py
# views

@require_POST #  URL에 직접 접근하거나 GET 요청을 통해 로그아웃을 시도하는 것을 방지
def logout(request):
    if request.user.is_authenticated: # 추가/ 로그인 상태일 때만 로그아웃 처리 / 로그아웃 처리에 보안을 강화 / 불필요한 로그아웃 시도를 방지
        auth_logout(request)
    return redirect("index")
```
```django
# html
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
### ?next=/ 사용하기
```py
 from django.contrib.auth.decorators import login_required   
# 전
if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    return redirect("index")
# 후
if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    next_url = request.GET.get("next") or "index" # 추가(?next=/ 부분 넣어주기)
    return redirect(next_url) # 추가

# html
<h1>login</h1>
<form action = "" method = "POST"> # action 지워서 ?next=/ 유도 복귀
{% csrf_token %}
{{form.as_p}}
<button type = "submit">login</button>
</form>