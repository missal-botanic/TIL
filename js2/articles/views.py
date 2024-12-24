# 표준 라이브러리
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# 서드파티 라이브러리
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# 애플리케이션의 모델 및 시리얼라이저
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer

        
class ArticleListAPIView(APIView):

    permission_classes = [IsAuthenticated]

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
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(reise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=204)

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





