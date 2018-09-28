from django.urls import path
from . import views

urlpatterns = [
    path('', views.FleetView.as_view(), name='fleet'),
]