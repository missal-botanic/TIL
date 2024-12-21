from django.urls import path
from . import views

app_name = "articles" # api는 잘 쓰지 않는다.
urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:article_pk>/", views.article_detail, name="article_detail" ) # name은 api에 잘 쓰지 않는다.
]
