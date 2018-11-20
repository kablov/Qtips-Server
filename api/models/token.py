from django.db import models
from django.utils.crypto import get_random_string
from api.models import *
import uuid


class Token(models.Model):
    class Meta:
        verbose_name = 'Токен аутентификации'
        verbose_name_plural = 'Токены аутентификации'

    def get_new_token():
        return get_random_string(length = 32)

    phone = models.OneToOneField(Phone, verbose_name = "Номер телефона", on_delete = models.DO_NOTHING)
    token = models.CharField("Токен", max_length = 100, blank = True, unique = True, default = get_new_token)

    def __str__(self):
        return str(self.phone) + " " + self.token

    def to_dict(self):
        result = {'token': self.token}
        return result
