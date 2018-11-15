from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True)
    phone = models.CharField("Номер телефона", validators=[MinLengthValidator(4)], max_length = 14, unique = True)
    name = models.CharField("Имя клиента", max_length = 100, blank = True)
    email = models.CharField("Адрес электронной почты", max_length = 100, blank = True, unique = True)
    photo = models.TextField("Ссылка на фото", blank = True, null = True)

    def __str__(self):
        return self.phone


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
