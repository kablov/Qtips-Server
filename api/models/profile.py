import random
from fcm_django.models import FCMDevice
from django.db import models
from django.core.validators import RegexValidator
from api.models import Phone


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_new_external_id():
        profiles = Profile.objects.all()
        existing_id_list = [profile.external_id for profile in profiles]
        external_id = random.SystemRandom().randint(100000, 999999)
        while external_id in existing_id_list:
            external_id = random.SystemRandom().randint(100000, 999999)
        return external_id

    status = [
        ('pure', 'Чистый'),
        ('banned', 'Забанен'),
    ]

    external_id = models.IntegerField(
        "Код сотрудника",
        validators=[RegexValidator(r'^\d{6}$')],
        unique=True,
        default=get_new_external_id
    )
    phone = models.OneToOneField(
        Phone,
        verbose_name="Номер телефона",
        on_delete=models.CASCADE,
        related_name='profile'
    )
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Email", max_length=100, blank=True, null=True)
    photo = models.TextField("Ссылка на фото", blank=True, null=True)
    status = models.CharField(
        "Статус",
        max_length=7,
        choices=status,
        default="pure"
    )
    qr = models.TextField("QR-код", blank=True, null=True)
    payment_url = models.CharField(
        "URL страницы оплаты",
        max_length=45,
        blank=True
    )
    balance = models.DecimalField(
        "Баланс",
        max_digits=8,
        decimal_places=2,
        default=0.00
    )
    test_balance = models.DecimalField(
        "Тестовый баланс",
        max_digits=8,
        decimal_places=2,
        default=0.00
    )
    are_notifications_enabled = models.BooleanField(
        "Уведомления включены?",
        default=False
    )
    fcm_devices = models.ManyToManyField(
        FCMDevice,
        verbose_name='Устройства',
        blank=True
    )

    def __str__(self):
        return "{0}) {1} {2}".format(str(self.external_id), self.first_name, self.last_name)
