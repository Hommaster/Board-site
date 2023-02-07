from django.urls import path
from .views import *


urlpatterns = [
    path('accounts/register/', RegisterUser.as_view(), name="register"),
    path('detail/<int:pk>/', ContentDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', ByRubricListView.as_view(), name="by_rubric"),
    path('', MainListView.as_view(), name="main"),
    path('accounts/logout/', logout_user, name="logout"),
    path('accounts/login/', LoginUser.as_view(), name="login")
]


#проверить работоспособность этой функции
