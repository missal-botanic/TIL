
```bash
conda create --name jg python=3.10
```

```bash
django-admin startproject my_first_pjt jg

django-admin startproject my_first_pjt jg . # 바닥에 파일 생성
```
```bash
python manage.py runserver
```

앱 생성
앱 등록
```py
# 앱 생성
python manage.py startapp articles # 앱 이름 복수형 권장

#settings.py 파일 33줄

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles', # 추가한 내용
]


models.py -> 데이터 베이스
views.py -> 데이터 처리 반환