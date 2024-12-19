from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    # birthdate = models.DateField(null=True, blank=True)  # 생년월일 필드 추가
    # phone_number = models.CharField(max_length=15, null=True, blank=True)  # 전화번호 필드 추가

