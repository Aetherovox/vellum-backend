from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet

router = DefaultRouter()
# router.register(r'auth/obtain',TokenObtainPairView,basename='token-obtain')
# router.register(r'auth/refresh',TokenRefreshView,basename='token-refresh')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/obtain', TokenObtainPairView.as_view()),
    path(r'auth/refresh', TokenRefreshView.as_view())
]
