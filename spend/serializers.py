from rest_framework import serializers
from .models import SpendStatistic


class SpendSerialiser(serializers.ModelSerializer):
    # revenue_field = serializers.SerializerMethodField()

    class Meta:
        model = SpendStatistic
        fields = ('date', 'spend', 'impressions', 'clicks', 'conversion',) # revenue

    # def get_revenue(self, obj):
    #     return obj.revenue_field.revenue
