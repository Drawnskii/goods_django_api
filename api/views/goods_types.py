from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..models import GoodsType
from ..serializer import GoodsTypeSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def list_goods_types(request):
    goods_types = GoodsType.objects.all()
    serializer = GoodsTypeSerializer(goods_types, many=True)
    return Response(serializer.data)