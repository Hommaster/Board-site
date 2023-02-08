from django.urls import path
from .views import *

users_urlpatterns = [
    path('accounts/register/', RegisterUser.as_view(), name="register"),
    path('accounts/logout/', logout_user, name="logout"),
    path('accounts/login/', LoginUser.as_view(), name="login"),
    path('accounts/users/profile/<int:pk>/', UserProfile.as_view(), name="profile")
]

