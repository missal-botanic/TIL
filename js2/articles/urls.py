from django.urls import path
from . import views

app_name = "articles" # api는 잘 쓰지 않는다.
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.AriticleDetailAPIView.as_view(), name="article_detail"), # name은 api에 잘 쓰지 않는다.
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDeleteAPIView.as_view(), name="comment_delete"),
]
