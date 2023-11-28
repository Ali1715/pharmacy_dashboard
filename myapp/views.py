from django.http import JsonResponse
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fechas
from .serializers import FechaSerializer
from django.views.decorators.http import require_http_methods
import json



@require_http_methods(["GET"])
def fechas_views(request):
    # If the request is GET, retrieve and display data
    fechas = Fechas.objects.all()
    serializer = FechaSerializer(fechas, many=True)
    
    # Extracting only the required fields from the serialized data
    fechas_data = [{"fecha_inicio": fecha["fecha_inicio"], "fecha_final": fecha["fecha_final"]} for fecha in serializer.data]

    response_data = {"fechas": fechas_data}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def fechas_views_post(request):
    # Handle the form submission logic here
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_final = request.POST.get('fecha_final')

    # Validate and process the form data as needed
    # Example: Save the form data to the database
    Fechas.objects.create(fecha_inicio=fecha_inicio, fecha_final=fecha_final)

    # Return a JsonResponse or redirect to a different page
    return JsonResponse({"message": "Form submitted successfully"})

def dashboard(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_grafico = [...]  

    return render(request, 'dashboard.html', {'datos_grafico': datos_grafico})
def dashboard_flexmonster(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_flexmonster = [...]  

    return render(request, 'dashboard_flexmonster.html', {'datos_flexmonster': datos_flexmonster})






def get_services_ia_api_months(request):
    # Hacer una solicitud a la API de Laravel para datos de productos próximos a vencer
    url_stock_product = 'http://34.151.236.58:3000/api/show/next-expired-products'
    response_stock_product = requests.get(url_stock_product)

    # Hacer una solicitud a la API de Laravel para datos de inventario total del mes
    url_total_inventory_month = 'http://34.151.236.58:3000/api/show/total-inventory/month'
    response_total_inventory_month = requests.get(url_total_inventory_month)

    # Hacer una solicitud a la API de Laravel para datos de ventas totales del mes
    url_total_sales_month = 'http://34.151.236.58:3000/api/show/total-sales/month'
    response_total_sales_month = requests.get(url_total_sales_month)

    # Hacer una solicitud a la API de Laravel para datos de tasa de obsolescencia del mes
    url_obsolencia_rate_month = 'http://34.151.236.58:3000/api/show/obsolencia-rate/month'
    response_obsolencia_rate_month = requests.get(url_obsolencia_rate_month)

    # Hacer una solicitud a la API de Laravel para datos de rotación de inventario del mes
    url_inventory_turnover_month = 'http://34.151.236.58:3000/api/show/inventory-turnover/month'
    response_inventory_turnover_month = requests.get(url_inventory_turnover_month)
    
    #http://34.151.236.58:3000/api/show/tendencia-temporada/month
    # Hacer una solicitud a la API de Laravel para datos de rotación de inventario del mes
    url_tendencia_temporada_month = 'http://34.151.236.58:3000/api/show/tendencia-temporada/month'
    response_tendencia_temporada_month = requests.get(url_tendencia_temporada_month)

    #http://34.151.236.58:3000/api/show/analisis-estacionalidad/month
    # Hacer una solicitud a la API de Laravel para datos de rotación de inventario del mes
    url_analisis_estacionalidad_month = 'http://34.151.236.58:3000/api/show/analisis-estacionalidad/month'
    response_analisis_estacionalidad_month = requests.get(url_analisis_estacionalidad_month)

    #url_predicciones_month = request.GET.get('urlWithParams', '')
    #response_predicciones_month = requests.get(url_predicciones_month)




    # Verificar si las solicitudes fueron exitosas y hay datos
    if (
        response_stock_product.status_code == 200 and
        response_total_inventory_month.status_code == 200 and
        response_total_sales_month.status_code == 200 and
        response_obsolencia_rate_month.status_code == 200 and
        response_inventory_turnover_month.status_code == 200 and
        response_tendencia_temporada_month.status_code == 200 and
        response_analisis_estacionalidad_month.status_code == 200 
        #response_predicciones_month.status_code == 200
        
    ):
        data_stock_product = response_stock_product.json()
        data_total_inventory_month = response_total_inventory_month.json()
        data_total_sales_month = response_total_sales_month.json()
        data_obsolencia_rate_month = response_obsolencia_rate_month.json()
        data_inventory_turnover_month = response_inventory_turnover_month.json()
        data_tendencia_temporada_month = response_tendencia_temporada_month.json()
        data_analisis_estacionalidad_month = response_analisis_estacionalidad_month.json()
       # data_predicciones_month = response_predicciones_month.json()
     
      

        # Imprimir los datos en la consola del servidor Django
        #print(data_stock_product)
        # Extract the "demanda" prediction data

        # Procesar los datos y enviarlos al contexto
        context = {
            'data_stock_product': data_stock_product.get('nextExpiredProducts', []),
            'data_total_inventory_month': data_total_inventory_month,
            'data_total_sales_month': data_total_sales_month,
            'data_obsolencia_rate_month': data_obsolencia_rate_month.get('obsolenceRate'),
            'data_inventory_turnover_month': data_inventory_turnover_month,
            'data_tendencia_temporada_month': json.dumps(data_tendencia_temporada_month.get('seasonalityAnalysis', [])),
            'data_analisis_estacionalidad_month': json.dumps(data_analisis_estacionalidad_month.get('seasonalityAnalysis', [])),
           # 'data_predicciones_month': response_predicciones_month.get('data', {}).get('prediccion', {}).get('demanda', {}).get('data', [])

       
            
        }
        return render(request, 'dashboard.html', context)
    else:
        return render(request, 'error.html', {'message': 'Error al obtener datos de la API'})
# views.py



def get_services_ia_api_pre(request):
    if request.method == 'GET':
        url_predicciones_month = request.GET.get('urlWithParams', '')

        # Hacer una solicitud a la URL recibida
        try:
            response_predicciones_month = requests.get(url_predicciones_month)
            response_data = response_predicciones_month.json()  # Suponiendo que la respuesta es JSON
            # Procesar los datos de la respuesta según sea necesario
            # ...

            return JsonResponse({'success': True, 'message': 'Solicitud exitosa.', 'data': response_data})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Error en la solicitud: {e}'})

    return JsonResponse({'success': False, 'error': 'Método de solicitud no válido.'})