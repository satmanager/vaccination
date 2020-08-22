from django.shortcuts import render


from rest_framework import viewsets

from .serializers import DrugSerializer
from .models import Drug

# Create your views here.

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all().order_by('name')
    serializer_class = DrugSerializer