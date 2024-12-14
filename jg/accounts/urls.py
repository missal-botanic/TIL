from django.urls import path
from . import views # from(폴더),import(파일)

app_name = 'accounts'
urlpatterns = [
    path('', views.accounts, name='accounts'), 
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
]