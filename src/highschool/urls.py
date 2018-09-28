from django.urls import path
from . import views

urlpatterns = [
    path('',views.HighSchoolView.as_view(), name='highschool'),
]