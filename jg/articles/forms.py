from django import forms

from articles.models import Article, Comment



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        #fields = ["title", "content"]
        #exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article",)
