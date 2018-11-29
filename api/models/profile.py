from django.db import models
from django.core.validators import RegexValidator
from api.models import *
from api.content import *
import random


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_new_external_id():
        external_id = random.SystemRandom().randint(100000,999999)
        if Profile.objects.filter(external_id = external_id).count() > 0:
            external_id = random.SystemRandom().randint(100000,999999)
            external_id_check(external_id)
        return external_id

    status = (
	('pure', 'Чистый'),
	('banned', 'Забанен'),
	)

    external_id = models.IntegerField(validators=[RegexValidator(r'^\d{6}$')], unique = True, default = get_new_external_id)
    phone = models.OneToOneField(Phone, verbose_name = "Номер телефона", on_delete = models.CASCADE)
    first_name = models.CharField("Имя", max_length = 50)
    last_name = models.CharField("Фамилия", max_length = 50)
    photo = models.TextField("Ссылка на фото", blank = True, null = True)
    status = models.CharField("Статус", max_length = 7, choices = status, default = "pure")
    qr = models.TextField("QR-код", blank = True, null = True)
    payment_url = models.CharField("URL страницы оплаты", max_length = 45, blank = True)
    balance = models.DecimalField("Баланс", max_digits = 6, decimal_places = 2, default = 0.00)
    test_balance = models.DecimalField("Тестовый баланс", max_digits = 6, decimal_places = 2, default = 0.00)

    def __str__(self):
        return str(self.external_id) + ") " + self.first_name + " " + self.last_name
