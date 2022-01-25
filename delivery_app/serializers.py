from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
import jwt


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Package
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if not any([user or user.is_active]):
            raise ValueError('Given credentials are wrong or user has been deactivated')
        return self.create_token(user)

    def create_token(self, user):
        return jwt.encode({'id': user.id}, settings.SECRET_KEY, algorithm='HS256')


class PasswordChangeSerializer(serializers.Serializer):

    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('new password') != attrs.get('new_password2'):
            raise serializers.ValidationError("Passwords does not match")
        return attrs

    def update_password(self, instance):
        instance.set_password(self.validated_data['new_password'])
        instance.save()
        return instance
