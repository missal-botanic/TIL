from django.urls import path
from . import views # from(폴더),import(파일)

urlpatterns = [
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('', views.users, name='users'), 
]