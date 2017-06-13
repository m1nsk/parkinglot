from rest_framework import serializers
from .models import AutoCard, CarOwner, CarModel, CarColor, Entry
import os


class AutoCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = AutoCard
        fields = '__all__'


class CarOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarOwner
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = '__all__'


class CarColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarColor
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = '__all__'