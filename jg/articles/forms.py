from django import forms

from articles.models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        #fields = ["title", "content"]
        #exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요
