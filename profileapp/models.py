from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # Profile과 user 객체를 하나씩 연결해준다.
    # on_delete : 이 user 객체가 delete 될 때 이와 연결되어있는 Profile 객체가 어떤 행동을 보일것인지를 담당
    # models.CASCADE : 이 Profile도 없어지게 하는것 (Django document 참고)
    # related_name : request.user.profile로 접근하는 이름 설정
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # 프로필 이미지
    # upload_to : media 밑에 profile이라는 경로에 이미지가 저장된다.
    # null=True : 프로필 이미지를 올리지 않아도 된다. (Null 값 허용이라는 뜻)
    image = models.ImageField(upload_to='profile/', null=True)

    nickname = models.CharField(max_length=20, unique=True, null=True)

    # 상태메시지
    message = models.CharField(max_length=100, null=True)
