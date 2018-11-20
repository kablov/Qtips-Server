from django.db import models
from django.core.validators import MinLengthValidator
from api.models import Phone


class SmsCode(models.Model):
    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'
    
    phone = models.OneToOneField(Phone, verbose_name = "Номер телефона", on_delete = models.CASCADE)
    code = models.CharField("Код", validators=[MinLengthValidator(4)], max_length = 4)

    def __str__(self):
        return "Номер: " + str(self.phone) + " Код: " + self.code
