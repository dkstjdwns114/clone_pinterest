from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile

        # 내가 사용할 필드들을 적어준다.
        fields = ['image', 'nickname', 'message']