from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:oven_id>', views.temps, name='temps')
]