from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from board.models import *
from d_r_f_main.permissions import *
from d_r_f_main.serializers import BbSerializer
from d_r_f_main.service import get_all_objects
# from rest_framework import viewsets


class BbAPIListView(generics.ListAPIView):
    queryset = get_all_objects(Bb)
    serializer_class = BbSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BbAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = get_all_objects(Bb)
    serializer_class = BbSerializer
    permission_classes = (IsOwnerOrReadOnly, )   # только для создателяя объявления или админа


class BbAPIDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_all_objects(Bb)
    serializer_class = BbSerializer
    permission_classes = (IsAdminOrReadOnly, )





# class BbViewSet(viewsets.ModelViewSet):
#     queryset = get_all_objects(Bb)
#     serializer_class = BbSerializer
#
#     # def get_queryset(self):
#     #     pk = self.kwargs.get("pk")
#     #     if not pk:
#     #         return get_all_objects(Bb)[::3]
#     #
#     #     return Bb.objects.filter(pk=pk)
#     # добавим новый маршрут с помощю декоратора.Маршрут генерирует роутер
#     @action(methods=['get'], detail=False)
#     def rubrics(self, request):
#         rubrics = get_all_objects(Rubric)
#         return Response({"Rubrics": [r.name for r in rubrics]})
#
#     @action(methods=['get'], detail=False)
#     def users(self, request):
#         users = get_all_objects(User)
#         return Response({"users": [[user.username, user.email] for user in users]})
#
#     @action(methods=["put", "get"], detail=True)
#     def rubric_change(self, request, pk=None):
#         rubric = Rubric.objects.get(pk=pk)
#         return Response({"rubric": rubric.name})
