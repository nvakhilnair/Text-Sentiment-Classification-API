from django.urls import path
from .views import InputTextViews

urlpatterns = [
    path('', InputTextViews.as_view())
]