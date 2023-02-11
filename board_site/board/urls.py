from django.urls import path

from d_r_f_main.urls import api_urlpatterns
# from d_r_f_main.views import BbViewSet
from d_r_f_users.urls import users_api_urlpatterns
from .views import *
from users.urls import users_urlpatterns
# !!!!!import cache_page for cache !!!!!!
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('detail/<int:pk>/', cache_page(60)(ContentDetailView.as_view()), name="detail"),
    path('update/<int:pk>/', cache_page(20)(BbEditView.as_view()), name='update'),
    path('add/', cache_page(10)(BbCreateView.as_view()), name='add'),
    path('<int:rubric_id>/', ByRubricListView.as_view(), name="by_rubric"),
    path('', MainListView.as_view(), name="main"),
] + users_urlpatterns
# api_urlpatterns + users_api_urlpatterns


# handler404 = PageNotFound404()