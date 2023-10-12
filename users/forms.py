from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import CustomUser, UserImage
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'groups')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'groups')

class UserImage(forms.ModelForm):
    class Meta:
        models = UserImage
        fields = ('image', 'user')