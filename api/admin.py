from django.contrib import admin
from .models import Location, GoodsType, Goods

# Register Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')  # Fields to display in the list view
    search_fields = ('name', 'location_type')  # Fields to search by
    list_filter = ('location_type',)  # Allow filtering by location type


# Register GoodsType model
@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the goods type
    search_fields = ('name',)  # Allow searching by the name


# Register Goods model
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'keeper', 'location', 'type')  # Fields to display in the list view
    search_fields = ('code', 'description')  # Fields to search by
    list_filter = ('keeper', 'location', 'type')  # Filters to allow narrowing down
    raw_id_fields = ('keeper', 'location', 'type')  # Use raw IDs for foreign key fields for easier selection
