from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Goods, Location, GoodsType

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required = True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class UserFirstNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'location_type']

class GoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = ['id', 'name']

class GoodsSerializer(serializers.ModelSerializer):
    keeper = UserSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    type = GoodsTypeSerializer(read_only=True)

    class Meta:
        model = Goods
        fields = ['code', 'description', 'keeper', 'location', 'type']