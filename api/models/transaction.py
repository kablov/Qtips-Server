from datetime import datetime
from django.db import models
from api.models import Profile


class Transaction(models.Model):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    type = (
	('tip_payment', 'Оплата чаевых'),
	('withdraw', 'Снятие со счета'),
	)

    recipient = models.ForeignKey(Profile, verbose_name="Кому", on_delete=models.CASCADE)
    amount = models.DecimalField("Сумма", max_digits=7, decimal_places=2, default=0.00)
    time = models.DateTimeField("Время", default=datetime.now)
    type = models.CharField("Тип транзакции", max_length=11, choices=type, default="tip_payment")
    cp_transaction_id = models.CharField("id транзакции в cloudpayments", max_length=50, blank=True)
    sa_transaction_id = models.CharField("id транзакции в нашем банке", max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

    def update_recipients_balance(self):
        profile = self.recipient
        transactions = Transaction.objects.filter(recipient=profile)
        profile.balance = sum(transaction.amount for transaction in transactions)
        profile.save(update_fields=['balance'])

    def save(self, *args, **kwargs):
        models.Model.save(self, *args, **kwargs)
        self.update_recipients_balance()
