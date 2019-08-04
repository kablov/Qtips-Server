from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token


class FCMTokenView(APIView):
    def post(self, request, format=None):
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        uuid = request.data['uuid']
        token = request.data['fcm_token']

        device_with_this_token = FCMDevice.objects.filter(
            registration_id=token
        ).first()
        device_with_this_uuid = FCMDevice.objects.filter(
            device_id=uuid
        ).first()

        if not device_with_this_token and not device_with_this_uuid:
            new_device = FCMDevice.objects.create(
                device_id=uuid,
                registration_id=token
            )
            profile.fcm_devices.add(new_device)
            profile.save()
            # Создан новый девайс

        elif device_with_this_token and device_with_this_uuid:
            if device_with_this_token != device_with_this_uuid:
                device_with_this_token.delete()
                device_with_this_uuid.registration_id = token
                device_with_this_uuid.save()
                """
                Девайс с таким же токеном удален, у девайса с таким же
                uuid перезаписаны поля user и token
                """
            else:
                device_with_this_uuid.save()
                # У девайса с таким же uuid перезаписано поле user

        elif not device_with_this_token and device_with_this_uuid:
            device_with_this_uuid.registration_id = token
            device_with_this_uuid.save()
            # У девайса с таким же uuid перезаписаны поля user и token

        return Response(status=status.HTTP_201_CREATED)


class DeleteDeviceIfLogoutView(APIView):
    def post(self, request, format=None):
        uuid = request.data['uuid']

        device = FCMDevice.objects.get(device_id=uuid)
        device.delete()
        # Девайс удален

        return Response(status=status.HTTP_201_CREATED)
