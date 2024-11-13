from rest_framework import serializers
from .models import *




class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'

class ShoeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeDetail
        fields = '__all__'