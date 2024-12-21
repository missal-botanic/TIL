from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Article
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework import status

HTTP_STATUS_201_CREATED = 201

@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        json_data = serializer.data
        return Response(json_data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #  return Response(serializer.errors, status=400)
            serializer.save()
            return Response(serializer.data, status=201) # 생략시 status=200 
        return Response(serializer.errors, status=HTTP_STATUS_201_CREATED)
    



@api_view(["GET", "PUT" ,"DELETE"])
def article_detail(request, article_pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True) # article이 instance(form) 역할
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=HTTP_STATUS_201_CREATED)
    
    elif request.method == "DELETE":
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_COaNTENT)
        
