from django.urls import path
from .views import SpendViews

urlpatterns = [
	path('', SpendViews.as_view()),
]
