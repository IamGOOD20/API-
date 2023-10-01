from rest_framework import generics
from .models import RevenueStatistic
from .serializers import RevenueSerializers


class RevenueView(generics.ListAPIView):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueSerializers
