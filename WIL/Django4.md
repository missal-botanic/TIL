
# drf 시작
```py
http://127.0.0.1:8000/api/v1/articles/ # 마지막에 '/' 꼭필요
```
```bash
# 랜덤 텍스트 채우기 설치
pip install django-seed
pip install psycopg2
```
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_seed', # 추가 
    'articles', # 보통 순서 (서드파디 -> 내부)
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
    path("html/", views.article_list_html, name="article_list_html"), 
    # http://localhost:8000/articles/html/
]
```
### json_01
```py
### articles / urls

path("json-01/", views.json_01, name="json_01"),


### articles / views

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
### json02
```py
### articles / urls

path("json-02/", views.json_02, name='json_02'),


### articles / views

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
### articles / serializers

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer): # 모듈 serializers에서 ModelSerializer상속
    class Meta:
        model = Article
        fields = "__all__"


### articles / views

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view(["GET"]) # 필수
def json_drf(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) # 단일 객체면 many=True 불필요 
    json_data = serializer.data # 불필요
    return Response(json_data)


```
```py
## test.py 포스트맨 역할
import requests

url = "http://127.0.0.1:8000/articles/json-drf/"
response = requests.get(url) 

print(response)
print(response.json())
```
## CRUD
### R
```py
urls 주로 루트 urls만 사용 name도 사용안함

### 루트 / urls

path('api/v1/articles/', include('articles.urls')), # api/v1/articles/

### articles / urls

path("", views.article_list, name="article_list"),


### articles /views

@api_view() # 기본값 GET, 리스트가 기본값 ["GET"]
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

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
### c
```py
# form으로 받거나 json으로 받거나

### articles / model

(null=True) , (auto_now=True) # POST 받지 안아도 된다.


### articles / urls

article 에서 POST로 중복 사용가능


### articles / views 1차

@api_view(["GET","POST"]) 
def article_list(request): # 추가
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST": # 이하 추가
        # data = request.POST.get("title")
        data = request.data
        title = data.get("title")
        content = data.get("content")
        article = Article.objects.create(title=title, content=content)
        return Response({})


### articles / views 2차

@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data) # 바로 serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) # 생략시 status=200 
        return Response(serializer.errors, status=400)


### status

HTTP_400_BAD_REQUEST = 400 # 수동으로

from rest_framework import status # 자동으로

@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 3차 (vaild return오류 생략시)
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) # 1차 수동으로
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 2차 자동으로
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
### articles / urls

article_detail 에서 POST로 중복 사용가능


### articles / views

@api_view(["GET", "PUT" ,"DELETE"])
def article_detail(request, article_pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT": # 수정용 코드
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
## class
```py
### articles / urls

path("", views.article_list, name="article_list"), # 전

path("", views.ArticleListAPIView.as_view(), name="article_list"), # 후 as_view()
path("<int:pk>/", views.AriticleDetailAPIView.as_view(), name="article_detail" )


### articles / views

class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by("-pk")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class AriticleDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Article, id=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(reise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=204)

# class base 는 다른 곳에 class 상속받기에 좋다.
```
2번 이상 반복은 하나로 뺸다
```bash
python manage.py seed articles --number=20 --seeder "Comment.article_id" 1 # 1번 아트클에 20개 생성
```
댓글
```py
### article / models

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


### article / Serializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

```
```py
# url
articles/<int:article_pk>/commnet/<int:comment_pk> 가능
```
```py
### articles / urls

path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
path("comments/<int:comment_pk>/", views.CommentDeleteAPIView.as_view(), name="comment_delete"),


### articles /views

class CommentListAPIView(APIView):
    def get_object(self, article_pk):
        return get_object_or_404(Article, id=article_pk)

    def get(self, request, article_pk):
        #comments = Comment.objects.filter(article_id=article_pk)
        article = self.get_object(article_pk)
        comments = article.comment_set.all() # 역참조
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_pk):
        article = self.get_object(article_pk)
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=201) # serializer.data 꼭 필요한것 아니다 {}가능
        
class CommentDeleteAPIView(APIView):

    def put(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

### delete + get_object

class CommentDeleteAPIView(APIView):
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=204)
```
## serialize 커스텀
```py
### articles / serializers 1차

from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) 


### articles / serializers 2차

from rest_framework import serializers
from .models import Article, Comment

# 정의 순서가 중요하다.
class CommentSerializer(serializers.ModelSerializer):# 모듈 serializers에서 ModelSerializer상속
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) # valid시 article 관련된것은 수정이 안되는 영역으로 바꾸어 그냥 통과

class ArticleSerializer(serializers.ModelSerializer): 
    comment_set = CommentSerializer(many=True, read_only=True) # 댓글과 글 동시 출력(오버라이딩)
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True) # 댓글 개수 출력(역참조 아님) comment_set.objects.all().count()

    class Meta:
        model = Article
        fields = "__all__"
```
```py
# 자주 쓰는 field 예시

from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days

```
```py
#댓글추가
#댓글 개수 추가
#특정 부분 빼기

# 정의 순서가 중요하다.

### articles / Serializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) 

    def to_representation(self, instance): # 추가
        ret = super().to_representation(instance)
        ret.pop("article") # article 제거
        return ret
        

class ArticleSerializer(serializers.ModelSerializer): 
    comment_set = CommentSerializer(many=True, read_only=True) 
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True) 

    class Meta:
        model = Article
        fields = "__all__"



### list에는 노댓글 detail만 댓글

class ArticleSerializer(serializers.ModelSerializer): 
    # 제거
    class Meta:
        model = Article
        fields = "__all__"


class ArticleDetailSerializer(ArticleSerializer): # 상속
    comment_set = CommentSerializer(many=True, read_only=True) # 하단에 추가
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True)


### articles / views 부분 수정
 
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article) # 변경
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True) # 변경
        if serializer.is_valid(reise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
```

```py
    'django_seed',
    'rest_framework',
    'accounts', # 추가
    'articles',

python manage.py startapp accounts

AUTH_USER_MODEL = 'accounts.User'
```
JWT
```bash
pip install djangorestframework-simplejwt
```
```py
# setting
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}
```
```py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"

urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```
```py
http://127.0.0.1:8000/api/v1/accounts/signin/
{
    "username":"admin",
    "password":"admin1234"
}
```
```py
http://127.0.0.1:8000/api/v1/accounts/token/refresh/
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1MDI5OTgyLCJpYXQiOjE3MzUwMjkzMzgsImp0aSI6IjliYzZmNjM0MmU2NjQwYmQ5ZGIyZTY2ODQzZjgwNDk1IiwidXNlcl9pZCI6MX0.JXLdccgUgyyB8XeFmmedMqqPOO-tQTSKKltWXjJSRJA"
}
```
```py
SIMPLE_JWT = { # 추가
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_seed',
    'rest_framework_simplejwt.token_blacklist', # 추가
    'rest_framework',
    'articles',
    'accounts',
] 


python manage.py migrate # makemigrations 불필요

# 한번 refesh된 토큰은 블랙리스트 등록
```
접근제한
```py
class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by("-pk")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
...

class ArticleListAPIView(APIView):

    permission_classes = [IsAuthenticated] # 추가

    def get(self, request):
        articles = Article.objects.all().order_by("-pk")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
...
```
```py
print(request.user.username) # 로그인한 유저 확인
```
ORM
```py

python manage.py startapp products
settings = "products",
#
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Fruit"),
        ("V", "Vegetable"),
        ("M", "Meat"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()# IntegerField 음수도 가능
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=1, choices = CATEGORY_CHOICES)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate
python manage.py seed products --number=30
```
```py
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When

Product.objects.all()

Product.objects.all().count()
```
#### Q() 를 이용해서 여러 조건 연결하기

```py
# & : and, | : or, ~ : not 연산자 활용 가능!
gt
gte
lt
lte

Product.objects.filter(Q(price__gt=15000) | Q(quantity__lt=3000))

products = Product.objects.filter(Q(price__gt=15000) | Q(quantity__lt=3000))

products.count()
products[0].id
```
### F() 를 이용해서 필드값 가져오기
```py
for문 처리를 대신

Product.objects.update(price = F('price') + 1000) # db 바뀐다
```
### annotate() 를 사용해서 추가 정보 제공하기 == 주석을 달다
```py
.all # 생략
.filter # 사용해서 특정 db만 적용 가능

product = Product.objects.annotate(total_price=F('price') * F('quantity')) # db 바뀌지 않는다.

product[0].total_price

```

aggregate() 를 사용해서 쿼리하기
```py
.all # 생략
.filter # 사용해서 특정 db만 적용 가능

# Avg, Sum, Count

Product.objects.aggregate(Avg('price')) # 자동 키값 
>>> {'price__avg': 20159.4}

Product.objects.aggregate(my_avg = Avg('price')) # 
>>> {'my_avg': 20159.4}


>>> 30
```
### group
```py

Product.objects.aggregate(Count('category'))
>>>30

Product.objects.aggregate(catagory_count = Count('category'))
>>>{'catagory_count': 30}


# .values 먼저 실행

Product.objects.values('category') # 1 내가 원하는 컬럼만 뽑기 전처리

Product.objects.values('category').annotate(Count('category')) # 2

Product.objects.values('category').annotate(catagory_count = Count('category')) # 3
>>> <QuerySet [{'category': 'F', 'catagory_count': 6}, {'category': 'M', 'catagory_count': 8}, {'category': 'O', 'catagory_count': 6}, {'category': 'V', 'catagory_count': 10}]>

```
## 최적화
```py
comments = Comment.objects.all()
for comment in comments:
	print(comment.article.title)

# 정참조
@api_view(["GET"])
def check_sql(request):
    comments = Comment.objects.all()
    for comment in comments:
        print(comment.article.title)
    #return Response(status=200)
    return Response() # 자동 200

# 역참조 (자신의 model 에서 없는 정보를 가지고 올때)
@api_view(["GET"])
def check_sql(request):
    articles = Article.objects.all().prefetch_related("comments")
    for article in articles:
        comments = article.comment.all() 
        for comment in comments: # +a번 추가 쿼리
            print(comment.content)
    return Response()


@api_view(["GET"])
def check_sql(request):
    from django.db import connection # 추가
    comments = Comment.objects.all()
    for comment in comments:
        print(comment.article.title)
    print("-"*30)
    print(connection.queries) # 추가
    return Response()
```
select_related # 정참조

prefetch_related # 역참조 2번의 쿼리 사용
```py
@api_view(["GET"])
def check_sql(request):
    from django.db import connection
    comments = Comment.objects.all().select_related("article") # 추가
    for comment in comments:
        print(comment.article.title)
    print("-"*30)
    print(connection.queries)
    return Response() 
```
```bash
pip install django-silk

MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware', # 추가
    ...
]

INSTALLED_APPS = (
    ...
    "silk", # 추가
)

path("check-sql/", views.check_sql, name= "check_sql"),

python manage.py migrate

python manage.py collectstatic # 불필요

http://127.0.0.1:8000/silk/
```
캐시
```
#
urlpatterns = [
    path("", views.product_list, name='products')
]


#
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


#
@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#
from django.core.cache import cache # 추가

@api_view(["GET"])
def product_list(request):
    cache_key = "product_list" # 
    print(cache_key)

    if not cache.get(cache_key): # 캐시에 없을 경우
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set(cache_key, json_response, 10) # key, value cache.set(cache_key, json_response, 5) 캐시 5초 만료
    
    response_data = cache.get(cache_key)
    return Response(response_data)
```
외부 api 사용
```py

### 방법 1
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from openai import OpenAI

class TranslateAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)

        system_instructions = """
        이제부터 너는 영어, 한글 번역가야.
        지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘.
        프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
        """

        # OpenAI API 요청
        completion = CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_message},
            ]
        )

        # 응답 가져오기
        chatgpt_response = completion.choices[0].message['content']

        return Response({"message": chatgpt_response})



### 방법 2_1 translate_bot()
from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPEN_API_KEY)


def translate_bot(message):
    instructions = """
    이제부터 너는 "영어, 한글 번역가"야. 
    지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
    프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
    """
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content


### 벙법 2-2 views 
from rest_framework.views import APIView
from rest_framework.response import Response
from .bots import translate_bot


class TranslateAPIView(APIView):

    def post(self, request):
        data = request.data
        message = data.get("message", "")
        translated_message = translate_bot(message)
        return Response({"translated_message": translated_message}) # 키 : 값으로 변경
