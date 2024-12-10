from django.shortcuts import render
from .models import Article # 모델 연결
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

def new(request):# 화면 연출 효과만 존재
    return render(request, "new.html")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    # 새로운 article 저장
    Article.objects.create(title=title, content=content)
    return render(request, "create.html")


