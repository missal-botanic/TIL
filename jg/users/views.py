from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.

def profile(request, username):  # 후
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member" : member,
    }
    return render(request, "profile.html", context)

def users(request):
    return render(request, "users.html")


@require_POST
def follow(request, user_id): # 다른 유저
    if request.user.is_authenticated: # 본인
        member = get_object_or_404(get_user_model(), pk=user_id) # 전체 유저 모델 중 id
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists(): # 상태 팔로워 조회 / 내가 팔로워 중이 아닐 때
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username = member.username)
    else:
        return redirect("accounts/login")
    
