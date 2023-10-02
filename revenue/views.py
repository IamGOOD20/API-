from rest_framework import generics
from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializers


class RevenueView(generics.ListAPIView):
    '''display revenue data'''

    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializers
