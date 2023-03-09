# from rest_framework.views import APIView -> aip_class
# from rest_framework import generics -> for api_classTes
from board.models import *
from rest_framework import viewsets, permissions
from board.api.board.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@permission_classes((IsAuthenticatedOrReadOnly, ))
@api_view(["GET", "POST"])
def api_rubrics(request):
    if request.method == "GET":
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = RubricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticatedOrReadOnly(), ))
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def api_rubric_detail(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    if request.method == "GET":
        serializer = RubricSerializer(rubric, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = RubricSerializer(rubric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        rubric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




