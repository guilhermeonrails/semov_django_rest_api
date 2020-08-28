from rest_framework import serializers
from eletro.models import Eletro

class EletroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eletro
        fields = '__all__'