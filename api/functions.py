import random
from api.models import *


def external_id_check(external_id):
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.external_id == external_id:
            print (external_id)
            external_id = random.SystemRandom().randint(100000,999999)
            external_id_check(external_id)
            break

    return external_id
