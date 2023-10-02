from rest_framework import serializers
from revenue.models import RevenueStatistic
from .models import SpendStatistic

class RevueSerialiser(serializers.ModelSerializer):
    '''get revenue field from revenue models'''
    class Meta:
        model = RevenueStatistic
        fields = ('revenue',)

class SpendStatisticSerialiser(serializers.ModelSerializer):
    '''display spend statistic'''
    revenue = RevueSerialiser(many=True)

    class Meta:
        model = SpendStatistic
        fields = ('date', 'name', 'spend', 'impressions', 'clicks', 'conversion', 'revenue',)
