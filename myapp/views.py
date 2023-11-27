from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Factura
from django.core import serializers
import requests
from flask import Flask, render_template, jsonify
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
    
  #  @app.route('/api/stock-product')
def get_stock_product():
    # Hacer una solicitud a la API de Laravel para datos de stock de productos
    url_stock_product = 'http://144.22.133.47:8000/api/stock-product'
    response_stock_product = requests.get(url_stock_product)

    # Verificar si la solicitud fue exitosa y hay datos
    if response_stock_product.status_code == 200:
        data_stock_product = response_stock_product.json()
        return jsonify(data_stock_product)
    else:
        return 'Error al obtener datos de stock de productos:', response_stock_product.status_code

if __name__ == '__main__':
    app.run(debug=True)