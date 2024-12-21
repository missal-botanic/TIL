```py
# form
# namespace
# account
# ?next=/ 
# @require_POST
# @login_required 
# 회원가입
# 로그인
# 로그아웃
# STATIC
# 파일 업로드
# amin
```
# djang.forms
```py
apps - forms.py 생성
```
```py
### articles / forms

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


### articles / views

def create(request):
    form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
    if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
        article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
        return redirect("article_detail", article.pk)
    return redirect("new")


### article / html

<form action="{% url 'create' %}" method="POST"> # views.create로 보냄
    {% csrf_token %}
    {{ forms.as_p}} # 추가
    <button type="submit" class="btn btn-primary">제출</button>
</form>
  <a href = {% url 'articles' %}>뒤로</a>
```

### new +> create 통합 가능, 이름 변경

```py
### articles / forms

from django import forms
from articles.models import Article # 모델 호출

class ArticleForm(forms.ModelForm): # 이름 변경가능
    class Meta: # forms.ModelForm의 오버라이딩으로 Meta 이름 변경 불가능
        model = Article
        fields = "__all__" # or fields = ["title", "content"]
        exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요


### articles / views

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

### edit +> update 통합 가능, 이름 변경

```py
# instance 가 없으면 생성
# instance = article 있으면 수정

### articles / views

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


### articles / html

<input type='text' id='title' name='title' value = "{{article.title}}"><br> # 전

{{ form.as_p }} # 후

```
# URL namespace
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

### articles / urls 상단에 추가

app_name = "articles" # namespace


### articles / html ':'추가

<form action="{% url 'create' %}" method="POST"> # 전
<form action="{% url 'articles:create' %}" method="POST"> # 후


### articles / views redirect 변경
return redirect("article_detail", article.pk) # 전
return redirect("articles:article_detail", article.pk) # 후

```
### Template Namespace
```py
# apps - templates 폴더에 article 폴더 추가
templates/articles
```
```py
### apps / view  return render() 변경

return render(request, "profile.html", context) # 전
return render(request, "articles/profile.html", context) # 후

```
# account
```bash
python manage.py createsuperuser
admin / adim1234
admin@test.com
```
### 로그인
```py
### articles / views  1차 로그인 화면 구성

from django.contrib.auth.forms import AuthenticationForm

def login(request):
    form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)


### articles / view  02차 실제 작동하게 구성

from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() # 중요
            auth_login(request, user) # 단축 가능
            return redirect("index")
        
    else:
        form = AuthenticationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)


### articles / html

<h1>login</h1>
<form action = "{% url "accounts:login" %}" method = "POST">
    {% csrf_token %}
    {{form.as_p}}
    <button type = "submit">login</button>
</form>
```
### 로그아웃
```py
### articles / urls

path('logout/', views.logout, name='logout'),


### articles / views

def logout(request):
    auth_logout(request) # 로그아웃
    return redirect("index")


### articles / html

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


# django way

from django.shortcuts import render, redirect, get_object_or_404 # 추가

def article_detail(request, pk):
    #article = Article.objects.get(id=pk) # 전
    article = get_object_or_404(Article, id=pk) # 변경
    context = {
        "article": article,
    }
    return render(request, "articles/article_detail.html", context)
```
## @require_POST 처리
```py
### articles / views 1차

from django.views.decorators.http import require_POST

@require_POST # POST 만 받는 경우, html 존재 하지 않는 경우, 분기점 필요 없음
def logout(request):
    auth_logout(request)
    return redirect("index")


### articles / views 2차

@require_POST #  URL에 직접 접근하거나 GET 요청을 통해 로그아웃을 시도하는 것을 방지
def logout(request):
    if request.user.is_authenticated: # 추가/ 로그인 상태일 때만 로그아웃 처리 / 로그아웃 처리에 보안을 강화 / 불필요한 로그아웃 시도를 방지
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


### articles / html

{% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">글쓰기</a>
{% else %}
    <a href="{% url "accounts:login" %}">로인그하고 작성하기</a>
{% endif %}

```
```py
### articles / html

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
## ?next=/ 사용하기
```py
 from django.contrib.auth.decorators import login_required   


# 전

if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    return redirect("index")


# 후

@login_required # 로그인해야 한는 곳에 비로그인 접근시 사용
if form.is_valid():
    user = form.get_user()
    auth_login(request, user)
    next_url = request.GET.get("next") or "index" # 추가(?next=/ 부분 넣어주기)
    return redirect(next_url) # 추가


### articles / html

<h1>login</h1>
<form action = "" method = "POST"> # action 지워서 ?next=/ 유도 복귀
    {% csrf_token %}
    {{form.as_p}}
<button type = "submit">login</button>
</form>
```
### @login_required 유/무
```py
# 수동 차단
@require_http_methods(["GET", "POST"])
def create(request):
    if not request.user.is_authenticated: # 로그인 상태가 아닌경우 돌리기 + url(get) 접근 차단
        return redirect("account:login")
    if request.method == "POST":
        form = ArticleForm(request.POST) 
        if form.is_valid(): 
            article = form.save() 
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "articles/create.html", context)

#자동 차단
@login_required # url(get)방식 접근 차단 기본값은 accounts/login
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "articles/create.html", context)
```

```py
# 전

def delete(request, pk):
    if request.method == "POST": # @require_POST 사용시 삭제
        article = get_object_or_404(Article, id=pk)
        article.delete()
        return redirect("articles:articles") # @require_POST 삭제
    return redirect("articles:article_detail", pk)


# 후

@login_required # 삭제 필요. next가 get 요청.
@require_POST
def delete(request, pk):
    if request.user.is_authenticated: # @login_required 삭제 이후에도 로그인 사용자가 사용하기 위함
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")
```
## 회원 가입
```py
### accounts / views 01 GET용 1차

def signup(request):
    form = UserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html",context)


### accounts / views 02 POST용 추가 2차

@require_http_methods(["GET", "POST"])# 리스트 화 필수
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # 바이딩 폼
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html",context)


### accounts / views 자동로그인 추가 3차

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save() # 변경(model form은 save 하는 순간 자신의 instance를 돌려준다 ex pop)
            auth_login(request, user) # 자동로그인 추가
            return redirect("index")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html",context)
```
### 회원 삭제
```py
### accounts / views

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # 세션도 삭제(위 아래 순서조심)
    return redirect("index")
```
### 회원 수정
```py
### accounts / views 1차 get

@require_http_methods(['GET', 'POST'])
def update(request):
    form = UserChangeForm(instance = request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)

```
## 커스텀 회원가입
```py
### accounts / forms 추가

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    password = None # 함수 분석 이후 덮어쓰기!(필요시 사용)
    class Meta: # 오버라이딩
        model = get_user_model() # 활성호된 유저만 불러오는 장고 함수
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


### accounts / views 2차 커스텀 버전으로 변경
@require_http_methods(['GET', 'POST'])
def update(request):
    form = CustomUserChangeForm(instance = request.user) # 변경
    context = {"form":form}
    return render(request, "accounts/update.html", context)

### accounts / view 3차 POST 추가
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user) # instance
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)
```
### 회원 비번 변경
```py
# user 필수 확인

def __init__(
    self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any
) -> None: ...


### accounts / view 1차 비번 변경 

@require_http_methods(["GET", "POST"])
def change_password(request):
    if request == "POST":
        form = PasswordChangeForm(request.user, request.POST) # request.user, request.POST 순서
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form":form}
    return render(request, "accounts/change_password.html", context)


### accounts / view 2차 비번 변경

@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # 변경 후에도 세션 자동 변경해서 로그인 유지
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)
```
# 미디어 업로드 (STATIC, MADIA)
### STATIC_URL
```py
### settings

#실제 주소가 아닌 URL만 존재
STATIC_URL = 'static/' # ex mystatic/ 으로 바꾸면 작동도 하고 웹에서 주소가 mystatic으로 시작한다. 
STATIC_ROOT = BASE_DIR / "staticfiles"  # 배포 때 사용
STATICFILES_DIRS = [BASE_DIR / "static"] # 공통의 경우 찾는 루트를 static로 지정
```
```py
apps/static/apps # 폴더 생성
```
```py
### 루트 html
{% load static %}
<img src="{% static "articles/image.png" %}">
```

## css
Media files 추가내용
```py
# settings 
MEDIA_URL = "/media/" # urls if settings.DEBUG: 디버깅 모드 추가시 , 이 다음 부터 루트는 디버깅 강제 루트 settings.MEDIA_ROOT에서 찾기(미디어 경로)
MEDIA_ROOT = BASE_DIR / "media" # 공통 실제 저장 경로

#DB 에는 경로 저장
```
```bash
my_first_pjt(루트)/static/css/style.css # 폴더 + 파일 생성
```

```django
<!-- html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 추가부분 start -->
    <link rel="stylesheet" href="{% static "css/style.css" %}}"> 
    <!-- 추가부분 end -->
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    {% block header %}
    {% endblock header %}
```
```css
/* css */
.img-200{
  width: 200px;
}
```
```py
### html
<img src="{% static "articles/image.png" %}" class="img-200">
```
## 유저업로드 파일 (static file 제외)

```bash
# 설치        
pip install pillow
```
```py
### 루트 / url 하단 추가분
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# 디버그 상태일 때 파일접근 가능하게

### articles / model 1차 추가분
class Article(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField() # 추가 # fileField 상속받은 함수

### articles / model 2차 추가분
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to = "images/",
        blank = True # 빈 이미지 가능
    )
# 마이그레이션 이후 템플릿 화면에 자동으로 출력
```
```py

### articles / views 파일 추가 코드

def create(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) # 추가


# articles / create.html

<form ation="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data"> # 추가


# articles / detail.html

{% if article.image %} # 이미지가 없을 경우 오류 생성방지
    <img src="{{ article.image.url }}" alt="">
{% endif %} # 출력화면

<img src="{% static "articles/image.png" %}"> # static과 다름
>>>
# 이미지 올리면 자동으로 media/images 폴더 생기고 이미지 저장 
# 모델에 upload_to = "images/" 이렇게 명령 했기 때문
```
# admin
```py
장소 adim 최소 권한은 staff부터

# 1차 apps - admin.py
admin.site.register(Article) # 기본값

# 2차 apps - admin.py
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at") # 표에서 보이는 행
    search_fields = ("title", "content") # 검색창 추가하고 검색 되는 부분이 제목과 내용
    list_filter = ("created_at",) # 오른쪽에 날짜 필터 생성
    date_hierarchy = "created_at" # 상단에 시간 필터
    ordering = ("-created_at",) # 정렬 순서
```

