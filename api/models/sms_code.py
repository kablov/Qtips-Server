from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from api.models import Phone


class SmsCode(models.Model):
    class Meta:
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'

    def get_new_code():
        return get_random_string(length = 4, allowed_chars = '1234567890')

    phone = models.OneToOneField(Phone, verbose_name = "Номер телефона", on_delete = models.CASCADE)
    code = models.CharField("Код", validators=[MinLengthValidator(4)], max_length = 4, default = get_new_code)
    udid = models.CharField(max_length = 36, blank = True)

    def __str__(self):
        return "Номер: " + str(self.phone) + " Код: " + self.code
