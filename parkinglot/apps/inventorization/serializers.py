from rest_framework import serializers
from .models import Inventorization
import os


class InventorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventorization
        fields = '__all__'
