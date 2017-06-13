from django.shortcuts import render
from .models import AutoCard, CarOwner, CarModel, CarColor, Entry
from .serializers import AutoCardSerializer, CarColorSerializer, CarModelSerializer, CarOwnerSerializer, EntrySerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.


class AutoCardViewSet(viewsets.ModelViewSet):
    queryset = AutoCard.objects.all()
    serializer_class = AutoCardSerializer
    permission_classes = (AllowAny,)


class CarOwnerViewSet(viewsets.ModelViewSet):
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer
    permission_classes = (AllowAny,)


class CarColorViewSet(viewsets.ModelViewSet):
    queryset = CarColor.objects.all()
    serializer_class = CarColorSerializer
    permission_classes = (AllowAny,)


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny,)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (AllowAny,)