from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html") # html 렌더링

def users(request):
    return render(request, "users.html")

def logins(request):
    return render(request, "logins.html")

def hello(request):
    name = "희경",
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]


    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,

       
    }
    return render(request, "hello.html", context)

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