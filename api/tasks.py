from django.core.mail import send_mail
from qtips.celery import app
from api.models import Profile


@app.task
def send_balance_info():
    profile = Profile.objects.get(external_id = 538660)
    send_mail(
        'Данные о балансе в Qtips',
        'Баланс на вашем счете в Qtips составляет ' + str(profile.balance) + ' рублей.',
        'maxim.kablov@gmail.com',
        [profile.email],
        fail_silently=False,
    )
