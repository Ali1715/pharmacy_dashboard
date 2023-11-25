from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Order
from django.core import serializers

# Create your views here.

import json

def grafico_view(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_grafico = [...]  

    return render(request, 'dashboard.html', {'datos_grafico': datos_grafico})
def pivot_data(request):
    dataset = [
        {
            'data': [10, 15, 20, 18, 25],
        }
    ]
    
    # Convierte el dataset a formato JSON
    #data = serializers.serialize('json', dataset)

    # Devuelve la respuesta JSON
    return JsonResponse({'dataset': dataset})