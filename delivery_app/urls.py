from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, UserRegistrationAPIView, LoginApiView, UserPasswordChange
from django.urls import path, include

router = DefaultRouter()

router.register(r'package', PackageViewSet)
router.register(r'registration', UserRegistrationAPIView, basename='user_register')
router.register(r'login', LoginApiView, basename='user_login')
router.register(r'password_update', UserPasswordChange, basename='user_password_update')

urlpatterns = [
    path('', include(router.urls)),
]
