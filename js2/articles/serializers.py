from rest_framework import serializers
from .models import Article, Comment

# 정의 순서가 중요하다.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) # valid시 article 관련된것은 수정이 안되는 영역으로 바꾸어 그냥 통과

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret
        
        

class ArticleSerializer(serializers.ModelSerializer): # 모듈 serializers에서 ModelSerializer상속
    class Meta:
        model = Article
        fields = "__all__"


class ArticleDetailSerializer(ArticleSerializer):
    comment_set = CommentSerializer(many=True, read_only=True) # 오버라이딩
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True) #역참조 아님 comment_set.objects.all().count()

    