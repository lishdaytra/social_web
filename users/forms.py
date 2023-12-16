from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import CustomUser, UserImage
from django.contrib.auth.models import Group
from django.contrib.auth.models import AnonymousUser


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'groups')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'groups')


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ('image',)
