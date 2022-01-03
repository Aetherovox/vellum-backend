from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .serializers import UserSerializer, PasswordChangeSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        return super(UserViewSet, self).create(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAuthenticated])
    def set_password(self,request,pk=None, *args, **kwargs):
        user = self.get_object()
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            # check old password was correct
            old_password = serializer.validated_data['old_password']
            if not user.check_password(old_password):
                # response will accept *args **kwargs so a message can be in dict format
                message = {"old_password":["Wrong Password"]}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # might want a custom failure code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# AUTHENTICATION VIEWS
class GoogleAuthView(SocialLoginView):
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter
    callback_url =

