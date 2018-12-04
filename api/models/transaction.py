from django.db import models
from api.models import *



class Transaction(models.Model):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    type = (
	('tip_payment', 'Оплата чаевых'),
	('withdrawal', 'Снятие со счета'),
	)

    to_user = models.ForeignKey(Profile, verbose_name = 'Кому', on_delete = models.DO_NOTHING)
    amount = models.DecimalField("Сумма", max_digits = 7, decimal_places = 2, default = 0.00)
    type = models.CharField("Тип транзакции", max_length = 11, choices = type, default = "tip_payment")

    def __str__(self):
        return str(self.id)
