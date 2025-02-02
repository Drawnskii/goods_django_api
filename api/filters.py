import django_filters
from django.db.models import Q
from .models import Goods

class GoodsFilter(django_filters.FilterSet):
    keeper_full_name = django_filters.CharFilter(method='filter_keeper_full_name', label='Keeper Full Name')

    class Meta:
        model = Goods
        fields = {
            'keeper': ['exact'],
            'location': ['exact'],
            'type': ['exact'],
            'description': ['icontains']
        }

    def filter_keeper_full_name(self, queryset, name, value):
        # Aquí manejamos el nombre completo con un espacio
        parts = value.split()  # Separar por espacios, en caso de que sea un nombre y apellido
        if len(parts) > 1:
            first_name, last_name = parts[0], " ".join(parts[1:])  # Asumimos que el primer nombre es la primera parte
            return queryset.filter(
                Q(keeper__first_name__icontains=first_name) & Q(keeper__last_name__icontains=last_name)
            )
        else:
            # Si solo hay un nombre (sin apellido)
            return queryset.filter(
                Q(keeper__first_name__icontains=value) | Q(keeper__last_name__icontains=value)
            )
