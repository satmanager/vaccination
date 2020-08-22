# serializers.py
from rest_framework import serializers

from .models import Drug

class DrugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drug
        fields = ('id','name', 'code', 'description')