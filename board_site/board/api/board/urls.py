from django.urls import path 
from .views import *


api_urlpatterns = [
        path('api/rubrics/', api_rubrics),
        path('api/rubrics/details/<int:pk>/', api_rubric_detail),
        ]
