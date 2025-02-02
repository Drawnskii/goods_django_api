from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from ..models import Goods, Location, GoodsType
from ..serializer import GoodsSerializer

from ..filters import GoodsFilter

from django.contrib.auth.models import User

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
    location_id = request.data.get('location')
    goods_type_id = request.data.get('type')

    location = Location.objects.filter(id=location_id).first()
    goods_type = GoodsType.objects.filter(id=goods_type_id).first()

    if not location or not goods_type:
        return Response(
            {"error": "Location or GoodsType not found"},
            status=status.HTTP_400_BAD_REQUEST
        )

    good = Goods.objects.create(
        code=request.data.get('code'),
        description=request.data.get('description'),
        location=location,
        type=goods_type,
        keeper=request.user
    )

    serializer = GoodsSerializer(good)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_good(request, pk):
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    location_id = request.data.get('location')
    goods_type_id = request.data.get('type')
    keeper_id = request.data.get('keeper')

    location = Location.objects.filter(id=location_id).first()
    goods_type = GoodsType.objects.filter(id=goods_type_id).first()
    keeper = User.objects.filter(id=keeper_id).first()

    if not location or not goods_type or not keeper:
        return Response({"error": "Location, GoodsType, or Keeper not found"}, status=status.HTTP_400_BAD_REQUEST)

    good.code = request.data.get('code', good.code)
    good.description = request.data.get('description', good.description)
    good.location = location
    good.type = goods_type
    good.keeper = keeper
    good.save()

    serializer = GoodsSerializer(good)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_good(request, pk):
    try:
        good = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)

    good.delete()
    return Response({"message": "Good deleted successfully"}, status=status.HTTP_204_NO_CONTENT)