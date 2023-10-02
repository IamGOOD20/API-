from rest_framework import serializers
from spend.models import SpendStatistic
from .models import RevenueStatistic

# class SpendDataSerialiser(serializers.ModelSerializer):
#     '''get impressions', 'click', 'conversion' from SpendStatistic model in Json format'''
#
#     class Meta:
#         model = SpendStatistic
#         fields = ('spend', 'impressions', 'clicks', 'conversion', )

class RevenueStatisticSerializers(serializers.ModelSerializer):
    '''display revenue statistic'''

    class Meta:
        model = RevenueStatistic
        fields = ('date', 'name', 'revenue', 'revenue', ) # 'impressions', 'click', 'conversion',
