from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:pk>/', ContentDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', ByRubricListView.as_view(), name="by_rubric"),
    path('', MainListView.as_view(), name="main")
]


#проверить работоспособность этой функции
