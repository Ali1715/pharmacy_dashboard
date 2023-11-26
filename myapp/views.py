from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Factura
from django.core import serializers
import requests
from django.shortcuts import render
from .models import Factura

# Create your views here.

import json

def dashboard(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_grafico = [...]  

    return render(request, 'dashboard.html', {'datos_grafico': datos_grafico})
def dashboard_flexmonster(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_flexmonster = [...]  

    return render(request, 'dashboard_flexmonster.html', {'datos_flexmonster': datos_flexmonster})




def datos_facturas(request):
    url_api = 'http://192.168.0.7:8000/api/facturas'
    response = requests.get(url_api)

    if response.status_code == 200:
        facturas_json = response.json()

        # Procesar los datos y enviarlos al contexto
        context = {
            'facturas_json': facturas_json,
        }

        return render(request, 'tu_template.html', context)
    else:
        return render(request, 'error.html', {'message': f'Error al obtener datos de la API: {response.status_code}'})