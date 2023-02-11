from django.urls import path
from .views import *

users_urlpatterns = [
    path('accounts/register/', RegisterUser.as_view(), name="register"),
    path('accounts/logout/', logout_user, name="log_out"),
    path('accounts/login/', LoginUser.as_view(), name="login"),
    path('accounts/users/profile/<int:pk>/', UserProfile.as_view(), name="profile"),
    path('accounts/users/change_password/', AUserPasswordChange.as_view(), name="change_password"),
    path('accounts/users/change_password/done/', password_change_done, name="password_done")
    # path('accounts/password_change/', UserPasswordChange.as_view(), name='password_change'),

]

