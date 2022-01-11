from rest_framework.serializers import ModelSerializer, CharField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import User

# want to be able to sign in with either username or email
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        credentials = {
            'email': '',
            'password':attrs.get('password')
        }
        user_obj = User.objects.filter(username=attrs.get('email')).first() or User.objects.filter(email=attrs.get('username')).first()
        if user_obj:
            credentials['email'] = user_obj.email

        return super().validate(credentials)


class UserSerializer(ModelSerializer):
    username = CharField(max_length=32)
    password = CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password',)
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PasswordChangeSerializer(ModelSerializer):
    old_password = CharField(min_length=8, required=True)
    new_password = CharField(min_length=8, write_only=True, required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

