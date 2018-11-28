from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError, PermissionDenied
from .exceptions import VerboseException


@csrf_exempt
def catch_errors(view_func):
    def _wrapped_view(request, *args, **kwargs):
        internal_code = None

        try:
            return view_func(request, *args, **kwargs)

        except ValidationError as e:
            reason = 'ValidationError'
            description = e.message
            http_code = 400

        except PermissionDenied as e:
            reason = 'PermissionDenied'
            description = 'You have no access ({})'.format(str(e))
            http_code = 401

        except ObjectDoesNotExist as e:
            reason = 'ObjectDoesNotExistError'
            description = str(e)
            http_code = 404

        except ValueError as e:
            reason = 'ValueError'
            description = str(e)
            http_code = 406

        except VerboseException as e:
            reason = 'BusinessLogicError'
            description = str(e)
            internal_code = e.code
            http_code = 409

        except Exception as e:
            reason = 'ServerError'
            description = str(e)
            http_code = 500

        response = JsonResponse(
            {
                'reason': reason,
                'description': description,
                'internal_code': internal_code,
            },
            status=http_code
        )

        return response
    return _wrapped_view
