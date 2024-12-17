1:N
```
작가(1) : 글(N)
1개의 글은 1개의 게시자를 가진다.
1개의 개시자는 N개의 게시물을 가진다.

댓글

글(1) : 댓글(n)
1개의 댓글은 1개의 게시자를 가진다.
1개의 글은 여러개의 댓글가능

A 테이블의 값이 / B 테이블 id와 매치(pk가 아닌 'article_id' 과 같이 생성)
```
```
models.ForeignKey(<참조하는 모델 클래스>, on_delete=<옵션>)
```
```py
apps - models
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # sql에서는 article_id로 변경 된다.(자동)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

```bash
python manage.py shell_plus
comment = Comment()
comment.content = “first comment”
comment.save()

>>> 댓글을 넣을 글을 선택하지 않음 (ex article = models.ForeignKey(Article, on_delete=models.CASCADE))
```
```bash
# 1 방법
article = Article.object.get(pk=1)
comment = Commnet()
comment.article = article
comment.content = "first comment"
comment.save()

# 2 방법
article = Article.object.get(pk=1)
comment.object.create(content="second comment", article=article) # 자동으로 sql의 _id 변경
```
```bash
article = Article.object.get(pk=1)
comment.article.title
comment.article.content
comment.article.created_at
```
```py
정참조(정방향 참조) : 댓글에서 글로 참조를 찾는것

역참조 : 글에서 댓글 찾기
_set : 매니저
comment_set : 역방향 참조 매니저

article = Article.objects.get(id=1)
article.comment_set.all # get, filter 가능
>>> 댓글 역참조 조회
```
```py
# 역참조 명령어 변경하기
article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") # comment_set 명령어 -> comments 변경
```

```py
path("<int:pk>/comment/", views.comment_create, name="comment_create"),

# 1차
@require_POST
def comment_create(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("articles:article_detail", pk)
# 2차
@require_POST
def comment_create(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) #데이터 베이스 저장 전 상태로 만들기 
        comment.article_id = pk
        comment.save()
        return redirect("articles:article_detail", pk)

# 3차
@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, id=pk) # 추가
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article # article로 변경
        comment.save()
        return redirect("articles:article_detail", article.pk) #article.pk

# 1차
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    comment_form = CommentForm() # 추가
    context = {
        "article": article,
        "comment_form" : comment_form, # 추가
    }
    return render(request, "articles/article_detail.html", context)

# 2차
def article_detail(request, pk):
    #article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all().order_by("-pk") # 오름차순
    context = {
        "article": article,
        "comment_form" : comment_form,
        "comments" : comments # 댓글 추가
    }
    return render(request, "articles/article_detail.html", context)

# html

    {% for comment in comments %} 
    <ul>
        <li>{{ comment.content }} | {{ comment.created_at }}
    </ul>
    {% endfor %}

```

