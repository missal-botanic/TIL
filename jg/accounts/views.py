from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def accounts(request):
    print("==================", request)
    return render(request, "accounts/accounts.html")

@require_http_methods(["GET", "POST"])
def login(request):
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

@require_POST
def logout(request):
    auth_logout(request)
    return redirect("index")

@require_http_methods(["GET", "POST"])# 리스트 화 필수
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # 바이딩 폼
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm() # 누군지 몰라도 되기에 request.user 없어도 됨
    context = {"form":form}
    return render(request, "accounts/signup.html",context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("index")

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


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)
