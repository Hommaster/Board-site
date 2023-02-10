from django.urls import path, include, re_path
from d_r_f_main.views import *

api_urlpatterns = [
    # аунтификация на основе Cookie sessions
    # (ДОБАВЛЯЕТСЯ .../login/  & .../logout/)
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    #
    # djoser
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/product/", BbAPIListView.as_view()),
    path("api/v1/product_update/<int:pk>/", BbAPIUpdateView.as_view()),
    path("api/v1/detail_product/<int:pk>/", BbAPIDeleteView.as_view()),
]
