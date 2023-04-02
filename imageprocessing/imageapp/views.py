from django.shortcuts import render
from rest_framework import viewsets
from .models import awsimage
from serializers import awsimageserializer

class awsimageview(viewsets.ModelViewSet):
    queryset=awsimage.objects.all()
    serializer_class=awsimageserializer

# Create your views here.
