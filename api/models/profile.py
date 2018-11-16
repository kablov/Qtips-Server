from django.db import models
from django.core.validators import RegexValidator
from api.models import Phone


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    status = (
	('pure', 'Чистый'),
	('banned', 'Забанен'),
	)

    external_id = models.IntegerField(validators=[RegexValidator(r'^\d{6}$')], unique = True)
    phone = models.OneToOneField(Phone, verbose_name = "Номер телефона", on_delete = models.CASCADE)
    first_name = models.CharField("Имя", max_length = 50)
    last_name = models.CharField("Фамилия", max_length = 50)
    photo = models.TextField("Ссылка на фото", blank = True, null = True)
    status = models.CharField("Статус", max_length = 7, choices = status, default = "pure")

    def __str__(self):
        return str(self.external_id) + ") " + self.first_name + " " + self.last_name
