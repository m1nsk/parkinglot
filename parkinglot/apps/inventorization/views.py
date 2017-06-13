from django.shortcuts import render
from .models import Inventorization
from .serializers import InventorizationSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.


class InventorizationViewSet(viewsets.ModelViewSet):
    queryset = Inventorization.objects.all()
    serializer_class = InventorizationSerializer
    permission_classes = (AllowAny,)