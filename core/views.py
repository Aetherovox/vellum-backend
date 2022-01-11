from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .serializers import UserSerializer, PasswordChangeSerializer, CustomObtainPairSerializer
from .models import User


# TODO: all password resets and email verifications in here. No cheating with dj_rest_auth
#   - get rid of dj_rest_auth and use allauth

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


class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

    def post(self, request, *args, **kwargs):
        usr_obj = User.objects.filter(username=request.data['username_or_email']).first() or \
                User.objects.filter(email=request.data['username_or_email']).first()
        if usr_obj:
            request.data['email'] = usr_obj.email
            _ = request.data.pop('username_or_email',None)
        else:
            print('User not found')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return Response({'Bad Request':f'Invalid Data: {request.data}'},status=status.HTTP_400_BAD_REQUEST)


# AUTHENTICATION VIEWS
class GoogleAuthView(SocialLoginView):
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter
    callback_url = ''


class TwitterAuthView(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
