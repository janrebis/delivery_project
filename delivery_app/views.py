import io
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Package
from .serializers import PackageSerializer, UserRegistrationSerializer, UserLoginSerializer
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
    authentication_classes = []
    permission_classes = []

    serializer_class = PackageSerializer
    queryset = Package.objects.all()


def generate_pdf(request):

    serializer = PackageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        sender = serializer.data['sender']
        recipent_name = serializer.data['recipent_name']
        recipent_surname = serializer.data['recipent_surname']
        street = serializer.data['street']
        house_number = serializer.data['house_number']
        apartment_number = serializer.data['apartment_number']
        city = serializer.data['city']
        country = serializer.data['country']

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100, 100, f"Sender: {sender}, /n Recipent: {recipent_name} {recipent_surname} /n Adress: {street} {house_number}/{apartment_number}/n {city}/n {country}")
        p.showPage()
        p.save()
        return response







