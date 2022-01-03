from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions
from django.conf import settings


# TODO: write tests for these

class Authentication(JWTAuthentication):
    @staticmethod
    def enforce_csrf(request):
        check = CSRFCheck()
        check.process_request(request)
        reason = check.process_view(request,None,(),{})
        if reason:
            raise exceptions.PermissionDenied(f'CSRF Failed: {reason}')

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        validated_token = self.get_validated_token(raw_token)
        self.enforce_csrf(request)
        return self.get_user(validated_token), validated_token
