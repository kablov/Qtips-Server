from fcm_django.models import FCMDevice
from api.models import Profile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class FCMTokenView(APIView):
    def post(self, request, format = None):
         profile_id = request.data['profile_id']
         uuid = request.data['uuid']
         token = request.data['FCM_token']
         profile = Profile.objects.get(id = profile_id)

         device_with_this_token = FCMDevice.objects.filter(registration_id = token).first()
         device_with_this_uuid = FCMDevice.objects.filter(device_id = uuid).first()

         if not device_with_this_token and not device_with_this_uuid:
             new_device = FCMDevice()
             new_device.device_id = uuid
             new_device.registration_id = token
             new_device.save()
             profile.fcm_devices.add(new_device)
             profile.save()
             print("Создан новый девайс")

         elif device_with_this_token and device_with_this_uuid:
             if device_with_this_token != device_with_this_uuid:
                 device_with_this_token.delete()
                 device_with_this_uuid.registration_id = token
                 device_with_this_uuid.save()
                 print("Девайс с таким же токеном удален, у девайса с таким же uuid перезаписаны поля user и token")
             else:
                 device_with_this_uuid.save()
                 print("У девайса с таким же uuid перезаписано поле user")

         elif not device_with_this_token and device_with_this_uuid:
             device_with_this_uuid.registration_id = token
             device_with_this_uuid.save()
             print("У девайса с таким же uuid перезаписаны поля user и token")

         return Response(status = status.HTTP_201_CREATED)


class DeleteDeviceIfLogoutView(APIView):
    def post(self, request, format = None):
        uuid = request.data['uuid']

        device = FCMDevice.objects.get(device_id = uuid)
        device.delete()

        return Response(status = status.HTTP_201_CREATED)
