from django.contrib.auth.forms import UserChangeForm, UserCreationForm # 추가
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # from .models import User 직접 모델 참조
        fields = UserCreationForm.Meta.fields + () # ex) ('nickname')

class CustomUserChangeForm(UserChangeForm):
    #password = None
    class Meta: # 오버라이딩
        model = get_user_model() # 활성호된 유저만 불러오는 장고 함수
        fields = [
            "first_name",
            "last_name",
            "email", 
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text

