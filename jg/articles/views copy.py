from django.shortcuts import render, redirect
from .models import Article # 모델 연결
from .forms import ArticleForm
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html") # html 렌더링

def users(request):
    return render(request, "users.html")

def logins(request):
    return render(request, "logins.html")

def data_throw(request):
    return render(request, "data-throw.html")

def data_catch(request): # 객체를 view 함수의 첫번째 인자로 받음(HttpResquest)
    message = request.GET.get("message") # "message" html name 부분
    context = {"message_v" : message}
    return render(request, "data-catch.html", context) # HttpResponse 전달

def profile(request, username):  # url 의 /내용 받음
    print(request)
    print(username)
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context)

def articles(request): # 처음 페이지 로딩시
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article": article,
    }
    return render(request, "article_detail.html", context)


def new(request):# 화면 연출 효과만 존재
    forms = ArticleForm()
    context = {"forms" : forms}
    return render(request, "new.html", context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content)
        return redirect("article_detail", article.pk)
    return redirect("new")

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(id=pk)
        article.delete()
        return redirect("articles")
    return redirect("article_detail", pk)

def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article" : article
    }
    return render(request, "edit.html", context)

def update(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.get(id = pk)
        article = Article.objects.create(title = title, content = content)
        return redirect("article_detail", article.pk) # request 없음
    return redirect("article_detail", article.pk)


# def update(request, pk):
#   article = Article.objects.get(pk=pk)
#   article.title = request.POST.get("title")
#   article.content = request.POST.get("content")
#   article.save()
#   return redirect("article_detail", article.pk)


    