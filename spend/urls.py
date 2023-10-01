from django.urls import path
from .views import SpendStatistic

urlpatterns = [
	path('', SpendStatistic.as_view()),
]
