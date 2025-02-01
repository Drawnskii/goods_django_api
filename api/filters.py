import django_filters
from .models import Goods

class GoodsFilter(django_filters.FilterSet):
    class Meta:
        model = Goods
        fields = {
            'keeper': ['exact'], 
            'location': ['exact'], 
            'type': ['exact'], 
            'description': ['icontains']
        }