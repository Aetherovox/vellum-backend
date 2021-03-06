from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, GoogleAuthView, TwitterAuthView, CustomObtainPairView

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/obtain', CustomObtainPairView.as_view()),
    path(r'auth/refresh', TokenRefreshView.as_view()),
    path(r'auth/social/login/google',GoogleAuthView.as_view(), name='google_login'),
    path(r'auth/social/login/twitter', TwitterAuthView.as_view(), name='twitter_login')
]
