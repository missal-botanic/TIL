from django.urls import path
from . import views # from(폴더),import(파일)


urlpatterns = [
    path('', views.articles, name = "articles"),
    path("new/", views.new, name = "new"),
    path("create/", views.create, name = "create"),
    path('data-throw/', views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"),
]