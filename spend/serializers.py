from rest_framework import serializers
from .models import SpendStatistic

class SpendSerialiser(serializers.ModelSerializer):

    class Meta:
        model = SpendStatistic
        fields = ('date', 'revenue', 'spend', 'impressions', 'clicks', 'conversion',)


        '''з поділом по дням (date) та назвою (name), 
        з агрегованими сумами значень revenue та пов'язаними значеннями spend, 
        impressions, clicks, conversion з моделі SpendStatistic.'''