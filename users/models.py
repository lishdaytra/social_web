from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.manager import CustomUserManager



class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина')
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='2000-01-01')
    first_name = models.CharField('Фамилия', max_length=150, blank=True)
    last_name = models.CharField('Имя', max_length=150, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Create your models here.
