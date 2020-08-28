from rest_framework import viewsets
from eletro.serializers import EletroSerializer
from eletro.models import Eletro

class EletroViewSet(viewsets.ModelViewSet):
    queryset = Eletro.objects.all()
    serializer_class = EletroSerializer

