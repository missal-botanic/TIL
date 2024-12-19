from django.urls import path
from . import views # from(폴더),import(파일)

app_name = "users"
urlpatterns = [
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('', views.users, name='users'), 
    path('<int:user_id>/follow/', views.follow, name='follow')
]