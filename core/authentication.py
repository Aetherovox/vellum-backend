from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        print(request.data)
        print(kwargs)
        cred = request.data.username_or_email
        try:
            user = User.objects.filter(email=cred).first() or User.objects.filter(username=cred).first()
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

