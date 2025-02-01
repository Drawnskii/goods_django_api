from django.urls import path
from .views import goods, users

urlpatterns = [
    path("login/", users.login, name="login"),
    path("register/", users.register, name="register"),
    path("profile/", users.profile, name="profile"),
    
    # Routes for goods management
    path("goods/", goods.create_good, name="create_good"),
    path("goods/<int:pk>/", goods.get_good, name="get_good"),
    path("goods/<int:pk>/edit/", goods.update_good, name="update_good"),
    path("goods/<int:pk>/delete/", goods.delete_good, name="delete_good"),
]
