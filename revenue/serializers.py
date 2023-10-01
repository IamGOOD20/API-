from rest_framework import serializers
from .models import RevenueStatistic


class RevenueSerializers(serializers.ModelSerializer):

    class Meta:
        model = RevenueStatistic
        fields = ('date', 'name', 'spend', 'revenue', ) # 'impressions', 'click', 'conversion',
