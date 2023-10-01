from django.urls import path
from .views import RevenueViev

urlpatterns = [
    path('', RevenueView.as_view())
]