from django.shortcuts import render


from rest_framework import viewsets

from .serializers import DrugSerializer, VaccinationSerializer
from .models import Drug
from .models import Vaccination

# Create your views here.

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all().order_by('name')
    serializer_class = DrugSerializer


class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all().order_by('date')
    serializer_class = VaccinationSerializer


