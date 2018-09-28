from django.urls import path
from . import views

urlpatterns = [
    path('',views.parents_list, name='parents_list'),
]