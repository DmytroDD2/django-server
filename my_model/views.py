from django.shortcuts import render

from rest_framework import viewsets

from .models import MyModel

from .serializer import MyModelSerializer


class MyModelItemViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
