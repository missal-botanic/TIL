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