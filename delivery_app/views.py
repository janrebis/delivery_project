from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.viewsets import ModelViewSet
from .serializers import PackageSerializer, UserRegistrationSerializer, UserLoginSerializer
from .models import Package


class PackageViewSet(ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()


class UserRegistrationAPIView(ViewSet):
    serializer_class = UserRegistrationSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.to_representation(user), status=status.HTTP_201_CREATED)


class LoginApiView(ViewSet):
    serializer_class = UserLoginSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save(), status=status.HTTP_200_OK)
