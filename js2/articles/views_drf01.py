# 표준 라이브러리
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# 서드파티 라이브러리
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

# 애플리케이션의 모델 및 시리얼라이저
from .models import Article
from .serializers import ArticleSerializer


@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all().order_by("-created_at")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True)  # data=request.data로 수정
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200) 
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=204)
        

