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
@login_required # 로그인해야 한는 곳에 비로그인 접근시 사용
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
```

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
회원 가입
```py
# 01 GET용
def signup(request):
    form = UserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html",context)

# 02 POST용
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

# 03 자동로그인 추가
@require_http_methods(["GET", "POST"])# 리스트 화 필수
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # 바이딩 폼
        if form.is_valid():
            user = form.save() # 변경(model form은 save 하는 순간 자신의 instance를 돌려준다 ex pop)
            auth_login(request, user) # 추가
            return redirect("index")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, "accounts/signup.html",context)
```
```py


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) # 세션도 삭제(위 아래 순서조심)
    return redirect("index")
```
수정
```py


from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    password = None # 함수 분석 이후 덮어쓰기!
    class Meta: # 오버라이딩
        model = get_user_model() # 활성호된 유저만 불러오는 장고 함수
        fields = [
            "first_name",
            "last_name",
            "email",
        ]



@require_http_methods(['GET', 'POST'])
def update(request):
    form = UserChangeForm(instance = request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)


@require_http_methods(['GET', 'POST'])
def update(request):
    form = CustomUserChangeForm(instance = request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)


@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)
```

```py

def __init__(
    self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any
) -> None: ...


@require_http_methods(["GET", "POST"])
def change_password(request):
    if request == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form":form}
    return render(request, "accounts/change_password.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # 변경 후 세션 자동 변경해서 로그인 유지
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)
