import io
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Package
from .serializers import UserLoginSerializer, UserRegistrationSerializer, PackageSerializer, PasswordChangeSerializer
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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


class PackageViewSet(ModelViewSet):

    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    @action(detail=True, methods=['get', ])
    def generate_pdf(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sticker.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100, 100, f"Sender: {instance.sender}, \n Recipent: {instance.recipent_name} {instance.recipent_surname} \n Adress: {instance.street} {instance.house_number}/{instance.apartment_number}\n {instance.city}\n {instance.country}")
        p.showPage()
        p.save()
        return response


class UserPasswordChange(ViewSet):
    serializer_class = PasswordChangeSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update_password(request)
        return Response('Password updated', status = status.HTTP_200_OK)


