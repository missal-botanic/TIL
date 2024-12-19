from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment # 모델 연결
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "articles/index.html") # html 렌더링

def users(request):
    return render(request, "articles/users.html")

def logins(request):
    return render(request, "articles/logins.html")

def data_throw(request):
    return render(request, "articles/data-throw.html")

def data_catch(request): # 객체를 view 함수의 첫번째 인자로 받음(HttpResquest)
    message = request.GET.get("message") # "message" html name 부분
    context = {"message_v" : message}
    return render(request, "articles/data-catch.html", context) # HttpResponse 전달

def profile(request, username):  # url 의 /내용 받음
    print(request)
    print(username)
    context = {
        "username" : username,
    }
    return render(request, "articles/profile.html", context)

def articles(request): # 처음 페이지 로딩시
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)

def article_detail(request, pk):
    #article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all().order_by("-pk") 
    #print(comments) # <QuerySet [<Comment: asdasasd>, <Comment: sdssd>, <Comment: 마드리드>, <Comment: real?>]>
    context = {
        "article": article,
        "comment_form" : comment_form,
        "comments" : comments
    }
    return render(request, "articles/article_detail.html", context)


@login_required # url(get)방식 접근 차단 기본값은 accounts/login
def create(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) # 데이터가 바인딩된 폼
        if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
            article = form.save(commit=False)
            article.author = request.user # form.save()도 작동하지만 진행을 위해 변수 지정
            article.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "articles/create.html", context)


@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")





def update(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {"form":form, "article" : article}
    return render(request, "articles/update.html", context)


@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, id=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) #데이터 베이스 저장 전 상태로 만들기 
        comment.article = article # 끼워 넣기
        comment.save()
        return redirect("articles:article_detail", article.pk)
    
@require_POST
def comment_delete(requset, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect("articles:article_detail", pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, id=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user) # 좋아요 취소
        else:
            article.like_users.add(request.user)
        return redirect("articles:articles")
    return redirect("accounts:login") # 미로그인시





# def new(request):# 화면 연출 효과만 존재
#     forms = ArticleForm()
#     context = {"forms" : forms}
#     return render(request, "new.html", context)
    
# def edit(request, pk):
#     article = Article.objects.get(id=pk)
#     context = {
#         "article" : article
#     }
#     return render(request, "edit.html", context)

# def update(request, pk):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         article = Article.objects.get(id = pk)
#         article = Article.objects.create(title = title, content = content)
#         return redirect("articles:article_detail", article.pk) # request 없음
#     return redirect("articles:article_detail", article.pk)


# def create(request):
#     form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
#     if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
#         article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
#         return redirect("article_detail", article.pk)
#     return redirect("new")


# def create(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         article = Article.objects.create(title=title, content=content)
#         return redirect("article_detail", article.pk)
#     return redirect("new")


# def update(request, pk):
#   article = Article.objects.get(pk=pk)
#   article.title = request.POST.get("title")
#   article.content = request.POST.get("content")
#   article.save()
#   return redirect("article_detail", article.pk)

