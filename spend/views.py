from rest_framework import generics
from .models import SpendStatistic
from .serializers import SpendSerialiser


class SpendViews(generics.ListAPIView):

    queryset = SpendStatistic.objects.all()
    serializer_class = SpendSerialiser




