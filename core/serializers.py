from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.password_validation import validate_password
from .models import User


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

