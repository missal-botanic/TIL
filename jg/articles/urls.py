from django.urls import path
from . import views # from(폴더),import(파일)

app_name = "articles"
urlpatterns = [
    path('', views.articles, name = "articles"),
    #path("new/", views.new, name = "new"),
    path("create/", views.create, name = "create"), # 페이지 없어도 명령어로 실행
    path('data-throw/', views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"), # 페이지 없어도 명령어로 실행
    # path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
    
]