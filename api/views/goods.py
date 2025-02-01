from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Goods, Location, GoodsType
from ..serializer import GoodsSerializer

from django.shortcuts import get_object_or_404


@api_view(['POST'])
def create_good(request):
    """
    Crear un nuevo bien.
    """
    location = Location.objects.filter(id=request.data['location']).first()
    goods_type = GoodsType.objects.filter(id=request.data['type']).first()

    if not location or not goods_type:
        return Response({"error": "Location or GoodsType not found"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = GoodsSerializer(data=request.data)

    if serializer.is_valid():
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

    location = Location.objects.filter(id=request.data.get('location')).first()
    goods_type = GoodsType.objects.filter(id=request.data.get('type')).first()

    if not location or not goods_type:
        return Response({"error": "Location or GoodsType not found"}, status=status.HTTP_400_BAD_REQUEST)

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
