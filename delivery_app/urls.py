from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, UserRegistrationAPIView, LoginApiView, generate_pdf
from django.urls import path, include

router = DefaultRouter()

router.register(r'package', PackageViewSet)
router.register(r'registration', UserRegistrationAPIView, basename='user_register')
router.register(r'login', LoginApiView, basename='user_login')

urlpatterns = {
    path('', include(router.urls)),
    path('pdf/<int:pk>', generate_pdf, name='generate_pdf')
}
