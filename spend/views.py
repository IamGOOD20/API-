from rest_framework import generics
from .models import SpendStatistic
from .serializers import SpendStatisticSerialiser, RevueSerialiser

class SpendStatisticView(generics.ListAPIView):
    '''display spend data'''
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerialiser
