from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from api.models import Profile



class Token(models.Model):
    class Meta:
        verbose_name = 'Токен аутентификации'
        verbose_name_plural = 'Токены аутентификации'

    def get_new_token():
        return get_random_string(length=32)

    profile = models.OneToOneField(Profile, verbose_name="Профиль", on_delete=models.DO_NOTHING)
    token = models.CharField("Токен", validators=[MinLengthValidator(32)], max_length=32,
                             unique=True, default=get_new_token)

    def __str__(self):
        return str(self.profile) + " " + self.token
