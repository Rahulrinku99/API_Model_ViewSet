from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework import viewsets
# Create your views here.

class ProdcutCrudMVS(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductMS