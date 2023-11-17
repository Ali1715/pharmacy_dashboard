from django.shortcuts import render

# Create your views here.

import json

def grafico_view(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_grafico = [...]  

    return render(request, 'grafico.html', {'datos_grafico': datos_grafico})
