## 1:N
```
글

작가(1) : 글(N)
1개의 글은 1개의 게시자를 가진다.
1개의 개시자는 N개의 게시물을 가진다.

댓글

글(1) : 댓글(n)
1개의 댓글은 1개의 게시자를 가진다.
1개의 글은 여러개의 댓글가능

A 테이블의 값이 / B 테이블 id와 매치(A테이블 pk와 연동되는 B 테이블 'article_id' 생성)
```
```py

models.ForeignKey(<참조하는 모델 클래스>, on_delete=<옵션>)
on_delete= # 글이 삭제 되었을 때 옵션

# articles / model
apps - models
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # sql에서는 article_id로 변경 된다.(자동)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# articles / forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article",) # 추가(모둔 리스트 뜨는것 방지)
```

```bash
# 커맨드로 생성 테스트
python manage.py shell_plus # shell 실행
comment = Comment() # 클래스로 객체 생성
comment.content = “first comment”
comment.save()

>>> 오류 댓글을 넣을 글을 선택하지 않음 '(ex article = models.ForeignKey(Article, on_delete=models.CASCADE))'
```
```bash
# 1 방법
article = Article.object.get(pk=1)
comment = Commnet()
comment.article = article
comment.content = "first comment"
comment.save()

# 2 방법
article = Article.object.get(pk=1)
comment.object.create(content="second comment", article=article) # 자동으로 sql의 _id 변경

# 출력
article = Article.object.get(pk=1)
comment.article.title
comment.article.content
comment.article.created_at
```
```py
정참조 : 댓글에서 글로 참조를 찾는것(정방향 참조) 
역참조 : 글에서 댓글 찾기

_set : 매니저
comment_set : 역방향 참조 매니저
```
```bash
# comment_set 예시
article = Article.objects.get(id=1)
article.comment_set.all # get, filter 가능
>>> 댓글 역참조 조회
```
```py
# 역참조 명령어 변경하기

# articles / model
article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") # comment_set 명령어 -> comments 변경

```

```py
# urls
path("<int:pk>/comment/", views.comment_create, name="comment_create"),

# 1차 views
@require_POST
def comment_create(request, pk):
    form = CommentForm(request.POST) # CommentForm은 form파일
    if form.is_valid():
        form.save()
        return redirect("articles:article_detail", pk) # 이 경우 새로고침 효과

# 2차 views
@require_POST
def comment_create(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) # 데이터 베이스 저장 전 상태로 만들기 
        comment.article_id = pk # article에 끼워 넣기
        comment.save()
        return redirect("articles:article_detail", pk)
# commit=False를 설정하면 데이터베이스에 바로 저장되지 않고, 객체만 생성된 상태로 반환됩니다. 이렇게 한 이유는 댓글 객체를 만들고 나서 article_id라는 추가 정보를 설정하기 위해서입니다. (댓글 객체를 만들고, 게시글 ID를 연결합니다.)

# 3차 article 사용시
@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, id=pk) # 추가
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article # article에 끼워 넣기
        comment.save()
        return redirect("articles:article_detail", article.pk) #article.pk

# article_detail 페이지 추가 내용

# 1차
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    comment_form = CommentForm() # 추가
    context = {
        "article": article,
        "comment_form" : comment_form, # 추가
    }
    return render(request, "articles/article_detail.html", context)

# 2차
def article_detail(request, pk):
    #article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all().order_by("-pk") # 오름차순 # comment를 불러온는 작업
    context = {
        "article": article,
        "comment_form" : comment_form,# 댓글 입력창
        "comments" : comments # 이미 입력된 댓글
    }
    return render(request, "articles/article_detail.html", context)

# html

    {% for comment in comments %} # comments는 뷰 변수/ comment는 comment_create의 객체
    <ul>
        <li>{{ comment.content }} | {{ comment.created_at }}
    </ul>
    
    {% endfor %}

```

## Custom UserModel

```
커스텀 유저 모델은 프로젝트 최초에 정의 하기를 권장한다.
유저모델은 연관되어 있는것이 많아서 DB연결 꼬이기 쉽다.
프로젝트 중간에 AUTH_USER_MODEL 바꾸는것 금지
```
```bash
# 마이그래이션 초기화

db.sqlite3 # 삭제
0001_initial.py # 마이그레이션은 다 체인으로 엮어있다.
0002_article_image.py
0003_comment.py

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```
```py
# settings
AUTH_USER_MODEL = 'accounts.User' # 'accounts.User'는 accounts 앱에 있는 User 모델을 사용하여 인증과 사용자 관리 기능을 처리하겠다는 설정
```
```py
# accounts / modesl
from django.contrib.auth.models import AbstractUser # 추가

class User(AbstractUser):
    pass

# accounts / form
from django.contrib.auth.forms import UserChangeForm, UserCreationForm # 추가

class CustomUserCreationForm(UserCreationForm): # 추가
    class Meta:
        model = get_user_model() # from .models import User 직접 모델 참조
        fields = UserCreationForm.Meta.fields + () # ex) ('nickname')


# accounts / views
from .forms import CustomUserChangeForm, CustomUserCreationForm # 추가

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # 변경 UserCreationForm -> CustomUserCreationForm
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm() # 변경 UserCreationForm -> CustomUserCreationForm
    context = {"form":form}
    return render(request, "accounts/signup.html", context)

# account / admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 추가
from .models import User # 추가

admin.site.register(User, UserAdmin)

```
## author 추가
```py

# articles / models
from django.conf import settings # 추가(author)

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = "images/", blank = True)

    author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles") # 추가 (AUTH_USER_MODEL 대신에 get_user_model 넣어도 작동한다.) + from django.contrib.auth import get_user_model 필요

    def __str__(self):
        return self.title


# articles / forms
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("author",) # 추가(모둔 리스트 뜨는것 방지)

# articles / views
@login_required 
def create(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) 
        if form.is_valid():
            article = form.save(commit=False) # 변경(저장 대기)
            article.author = request.user # 추가
            article.save() # 추가
            return redirect ("articles:article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "articles/create.html", context)
```
```py
{% if user == article.author %} # 해당 작성자만 보이게
작성자: {{ article.author }} # {{ article.author.username }} 작성자 이름 표시 
```
## Model Relationship (M:N)

한 명의 유저는 여러개의 게시글을 좋아할 수 있고
하나의 게시글도 여러명의 유저에게 좋아요를 받을 수 있다

중계테이블 필요

```py
# article / models
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    ) # -> user.like_articles.all() 접근 가능 / 미지정시 like_user_set 이 기본 매니저

# models.ManyToManyField 사용 하면 자동 중계테이블 생성
```
```
python manage.py makemigrations
python manage.py migrate
```
```bash
#  변수 지정
article_1 = Article.objects.get(id=1)
article_2 = Article.objects.get(id=2)

admin_user = User.objects.get(id=1)
test01_user = User.objects.get(id=2)

# 좋아요 누르기(양방향 가능)
article_1.like_users.add(admin_user)
article_2.like_users.add(test01_user)
article_1.like_users.remove(admin_user)
or
test01_user.like_articles.add(article_2)

# 조회
article_1.like_users.all()
article_2.like_users.all()

# 역조회
admin_user.like_articles.all() # related_name="like_articles"
test01_uesr.like_articles.all()
```
```py
path("<int:pk>/like/", views.like, name="like"), # <int:pk>는 pk부분을 추가로 넘긴다는 의미, view 함수에서 pk 인수 필요


@require_POST
def like(request, pk):
    if request.uesr.is_authenticated:
        article = get_object_or_404(Article, id=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_user.remove(request.user) # 좋아요 취소
        else:
            article.like_user.add(request.user)
        return redirect("articles:articles")
    return redirect("articles:login") # 미로그인시

# filter()와 exists()는 장고 ORM(Django Object-Relational Mapping) 문법

    <form action="{% url 'articles:like' article.pk %}" method="POST"># urls 에 pk 인수에 맞게 pk
        {% csrf_token %}
        {% if request.user in article.like_users.all %} # request.user 대신 user 도 가능
            <input type="submit" value="좋아요 취소">
        {% else %}
            <input type="submit" value="좋아요">
        {% endif %}
    </form>

 ## 팔로우 기능

 모델에서 'self' 사용
 symmetrical=True 사용가능 (기본값 True)# 팔로우 하면 자동 서로 팔로우 기능/ False 필요 / 친구 맺기에 필요


class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")


path('<int:user_id>/follow/', views.follows, name='follow') # 단수 사용



@require_POST
def follow(request, user_id): # 다른 유저
    if request.user.is_authenticated: # 본인
        member = get_object_or_404(get_user_model, id=user_id) # 전체 유저 모델 중 id
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists(): # 상태 팔로워 조회 / 내가 팔로워 중이 아닐 때
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username = member.username)
    else:
        return redirect("accounts/login")


def profile(request, username): # 전
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context)


def profile(request, username):  # 후
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member" : member,
    }
    return render(request, "profile.html", context)


<h1>{{username}} Profile</h1># 전
<h1>{{member.username}} Profile</h1># 후



{% if request.user != member %}# 후
    <form action="{% url "users:follow" member.pk %}" method="POST">
        {% csrf_token %}
            {% if request.user in member.followers.all %}
                <input type="submit" value="언팔로우">
            {% else %}
                <input type="submit" value="팔로우">
            {% endif %}
    </form>
{% endif %}