from rest_framework import serializers
from .models import awsimage


class awsimageserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=awsimage
        fields={'title','images'}