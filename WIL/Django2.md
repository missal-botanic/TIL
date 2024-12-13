```py
apps - forms.py 생성
```
```py
# apps - forms.py
from django import forms

class ArticleForm(forms.Form):
    GENRE_CHOICES = [
        ("techology", "Techology"),
        ("life", "Life"),
        ("hobby", "Hobby")
    ]
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    #genre = forms.ChoiceField(choices=GENRE_CHOICES)

# apps - html
{% extends 'base.html' %}

{% block content %}
  <form action="{% url 'create' %}" method="POST"> <!-- views.create로 보냄 -->
    {% csrf_token %}
    {{ forms.as_p}}
    <button type="submit" class="btn btn-primary">Primary</button>
  </form>

  <a href = {% url 'articles' %}>뒤로</a>
{% endblock %}
```

```py
# apps - views.py
def create(request):
    form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
    if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
        article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
        return redirect("article_detail", article.pk)
    return redirect("new")
```

new +> create # 통합 + 이름변경

```py
# apps - forms.py
from django import forms

from articles.models import Article

class ArticleForm(forms.ModelForm): # 이름 변경가능
    class Meta: # 이름 변경 불가능
        model = Article
        fields = "__all__"
        #fields = ["title", "content"]
        #exclude = ("title",) # __all__ 이후 예외 지정 / 괄호 확인 필요
```

```py
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) # 데이터가 바인딩된 폼
        if form.is_valid(): # 빈데이터 혹은 받지 않을 데이터 있을 경우 필터
            article = form.save() # form.save()도 작동하지만 진행을 위해 변수 지정
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm()
    
    context = {"form": form}
    return render(request, "create.html", context)
```



edit - update

```py
#instance 가 없으면 생성
#instance = article 있으면 수정

def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {"form":form, "article" : article}
    return render(request, "update.html", context)
```