
# drf 시작
```py
http://127.0.0.1:8000/api/v1/articles/ # 마지막에 '/' 꼭필요
```
```bash
pip install django-seed
pip install psycopg2
```
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_seed', # 추가 
    'articles', # 보통 서드파디 -> 내부 app 순서
]
```
```bash
python manage.py seed articles --number=30 # 랜덤 텍스트 채우기
```
```py

## articles / model

from django.db import models

class Article(models.Model): # 클래스는 단수
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


## roots / urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]

## articles / urls

from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("html/", views.article_list_html, name="article_list_html"), # http://localhost:8000/articles/html/
]
# views.article_list_html는 함수 이름 article_list_html 닉네임 articles/article_list.html 실제파일 이름이지만 url에서 쓰이지는 않음

## articles / views

def article_list_html(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, "articles/article_list.html", context)


## articles / html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Article</h2>
    <hr><br>

    {% for article in articles %}
    <h3>{{ article.title}}</h3>
    <p>{{article.content}}</p>
    <p>{{article.created_at}}</p>
    <p>{{article.updated_at}}</p>
    <hr>
    
    {% endfor %}
    
    
</body>
</html>
```
## json_01
```py
## articles / urls

path("json-01/", views.json_01, name="json_01"),


# articles / views
def json_01(request):
articles = Article.objects.all() # query set
json_res = []

for article in articles:
    json_res.append(
        {
        "title": article.title,
        "content": article.content,
        "created_at": article.created_at,
        "updated_at": article.updated_at,
        }
    )
return JsonResponse(json_res, safe=False) # 리스트일 경우 safe=False, 딕셔너리일 경우 기본값 사용(적지 않아도 됨)
```
## json02
```py
## articles / urls

path("json-02/", views.json_02, name='json_02'),


## articles / views

def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize("json", articles)
    return HttpResponse(res_data, content_type="application/json") 
    # return JsonResponse(json_res, safe=False) 이것도 가능
```

## serializers

```bash
pip install djangorestframework
```
```py
## articles / serializers

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer): # 모듈 serializers에서 ModelSerializer상속
    class Meta:
        model = Article
        fields = "__all__"

## articles / views

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer


@api_view(["GET"]) # 필수
def json_drf(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) # 단일 객체면 many=True제거 
    return Response(serializer.data)

```

```py
## test
import requests

url = "http://127.0.0.1:8000/articles/json-drf/"
response = requests.get(url) 

print(response)
print(response.json())
```
## CRUD

```py
urls 주로 루트 urls만 사용 name도 사용안함

#
path('api/v1/articles/', include('articles.urls')),

#
path("", views.article_list, name="article_list"),

#
@api_view() # 기본값 GET, 리스트가 기본값 ["GET"]
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    json_data = serializer.data
    return Response(json_data)
    #return Response(serializer.data)
```
```py
#
path("<int:article_pk>/", views.article_detail, name="article_detail" ) # name은 api에 잘 쓰지 않는다.

#
@api_view()
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```
# c
```py
form으로 받거나 json으로 받거나

# model
(null=True) , (auto_now=True)# POST 받지 안아도 된다.

## articles / urls
article 에서 POST로 중복 사용가능

##
@api_view(["GET","POST"]) 
def article_list(request): # 추가
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)
    elif request.method == "POST": # 이하 추가
        #data = request.POST.get("title")
        data = request.data
        title = data.get("title")
        content = data.get("content")
        article = Article.objects.create(title=title, content=content)
        return Response({})


@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) # 생략시 status=200 
        return Response(serializer.errors, status=400)


##

HTTP_STATUS_201_CREATED = 201 # from rest_framework import status

@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 변경
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=HTTP_STATUS_201_CREATED) # 변경

        # return Response(serializer.errors, status=status.HTTP_201_CREATED)
```
# d
```py
## urls

article_detail 에서 POST로 중복 사용가능
http://127.0.0.1:8000/api/v1/articles/33/ # 마지막 / 꼭필요
##

@api_view(["GET","DELETE"])
def article_detail(request, article_pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## u
```py
##
article_detail 에서 POST로 중복 사용가능

##
@api_view(["GET", "PUT" ,"DELETE"])
def article_detail(request, article_pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article, data=request.data) # article이 instance(form) 역할, partial=True 부분 수정 가능 제거시 모든 부분을 Json에 넣어야함(동일한 내용이라도)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=HTTP_STATUS_201_CREATED)
    
    elif request.method == "DELETE":
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_COaNTENT)
```