from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50) # max 무저건 필요
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)