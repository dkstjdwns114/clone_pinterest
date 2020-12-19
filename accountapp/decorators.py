from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# 현재 로그인되어있는 유저의 pk와 접속하려는 주소의 pk가 같은지 확인하는 decorator
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated