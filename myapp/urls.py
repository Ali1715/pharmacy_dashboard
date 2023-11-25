from django.urls import path
from . import views

urlpatterns = [
    path('', views.grafico_view, name='grafico_view'),
    path('data', views.pivot_data, name='pivot_data'),
]