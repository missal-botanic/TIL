from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50) # max 무저건 필요
    content = models.TextField(default='') # 빈문자열
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = "images/", blank = True)

    def __str__(self):
        return self.title