from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # CBV는 아래처럼 작성해야 FBV처럼 잘 작동한다.
    path('create/', AccountCreateView.as_view(), name='create'),
]