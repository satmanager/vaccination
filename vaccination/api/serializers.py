# serializers.py
from rest_framework import serializers

from .models import Drug
from .models import Vaccination

class DrugSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Drug
        fields = ('id','name', 'code', 'description','url')


class VaccinationSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Vaccination
        fields = ('id','rut', 'dose', 'date', 'drug')        