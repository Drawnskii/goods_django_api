from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from ..models import Goods, Location, GoodsType
from ..serializer import GoodsSerializer

from ..filters import GoodsFilter

class GoodsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filterset_class = GoodsFilter

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

@api_view(['GET'])
def get_good(request, pk):
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GoodsSerializer(good)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_good(request):
    location = Location.objects.filter(id=request.data['location']).first()
    goods_type = GoodsType.objects.filter(id=request.data['type']).first()

    if not location or not goods_type:
        return Response({"error": "Location or GoodsType not found"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = GoodsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_good(request, pk):
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
@permission_classes([IsAuthenticated])
def delete_good(request, pk):
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    good.delete()
    return Response({"message": "Good deleted successfully"}, status=status.HTTP_204_NO_CONTENT)