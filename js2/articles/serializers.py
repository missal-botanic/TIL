from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer): # 모듈 serializers에서 ModelSerializer상속
    class Meta:
        model = Article
        fields = "__all__"
