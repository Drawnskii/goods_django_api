from django.urls import path
from .views import goods, users
from .views.goods import GoodsListCreateAPIView 

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("register/", users.register, name="register"),
    path("profile/", users.profile, name="profile"),
    
    # Routes for goods management
    path("goods/", goods.create_good, name="create_good"),
    path("goods/<int:pk>/", goods.get_good, name="get_good"),
    path("goods/<int:pk>/edit/", goods.update_good, name="update_good"),
    path("goods/<int:pk>/delete/", goods.delete_good, name="delete_good"),
    path('goods/search/', GoodsListCreateAPIView.as_view(), name='goods_list_create'),
]
