from django.db import models
from django.core.validators import MinLengthValidator


class Phone(models.Model):
    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    country_code = models.CharField("Код страны", validators=[MinLengthValidator(2)], max_length = 4)
    number = models.CharField("Номер", validators=[MinLengthValidator(4)], max_length = 14)
    is_verified = models.BooleanField("Подтвержден?", default = False)

    def __str__(self):
        return str(self.country_code) + str(self.number)
