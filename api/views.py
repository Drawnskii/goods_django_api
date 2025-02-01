from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializer import UserSerializer
from .serializer import GoodsSerializer

from .models import Goods, Location, GoodsType

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username = request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user = user)

    serializer = UserSerializer(instance = user)

    return Response({"token": token.key, "user": serializer.data}, status = status.HTTP_200_OK)

@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user = user)
        
        return Response({'token': token.key}, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    print(request.user)

    return Response("You logged as {}".format(request.user.username), status = status.HTTP_200_OK)


@api_view(['POST'])
def create_good(request):
    """
    Crear un nuevo bien.
    """
    # Asegurarse de que la ubicación y el tipo de bien existen
    location = Location.objects.filter(id=request.data['location']).first()
    goods_type = GoodsType.objects.filter(id=request.data['type']).first()

    if not location or not goods_type:
        return Response({"error": "Location or GoodsType not found"}, status=status.HTTP_400_BAD_REQUEST)

    # Serializar los datos del nuevo bien
    serializer = GoodsSerializer(data=request.data)

    if serializer.is_valid():
        # Guardar el bien en la base de datos
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_good(request, pk):
    """
    Obtener los detalles de un bien.
    """
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GoodsSerializer(good)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_good(request, pk):
    """
    Editar los detalles de un bien.
    """
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    # Validar que la ubicación y el tipo de bien existen
    location = Location.objects.filter(id=request.data.get('location')).first()
    goods_type = GoodsType.objects.filter(id=request.data.get('type')).first()

    if not location or not goods_type:
        return Response({"error": "Location or GoodsType not found"}, status=status.HTTP_400_BAD_REQUEST)

    # Serializar y actualizar el bien
    serializer = GoodsSerializer(good, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_good(request, pk):
    """
    Eliminar un bien.
    """
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    good.delete()
    return Response({"message": "Good deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
