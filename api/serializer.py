from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Goods

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'code', 'description', 'keeper', 'location', 'type']