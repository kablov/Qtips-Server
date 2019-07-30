from api.models import Token
from qtips import settings
from qtips.exceptions import AccessDenied


def access_key_check(request):
    if request.META.get('HTTP_ACCESS_KEY') != settings.ACCESS_KEY:
        raise AccessDenied("Доступ запрещен")
