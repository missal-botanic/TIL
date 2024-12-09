from django.shortcuts import render

# Create your views here.

def profile(request, username):  # url 의 /내용 받음
    print(request)
    print(username)
    context = {
        "username" : username,
    }
    return render(request, "profile.html", context)

def users(request):
    return render(request, "users.html")