document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('tuFormulario');
    var fechaInicioInput = document.getElementById('fecha_inicio');
    var fechaFinalInput = document.getElementById('fecha_final');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var fechaInicio = fechaInicioInput.value;
        var fechaFinal = fechaFinalInput.value;

        var apiUrl = 'http://34.151.236.58:3000/api/show/prediction';
        var urlWithParams = apiUrl + '?fecha_inicio=' + fechaInicio + '&fecha_final=' + fechaFinal;

        // Enviar la URL al servidor
        fetch('/get_services_ia_api_pre/?urlWithParams=' + encodeURIComponent(urlWithParams), {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta si es necesario
            console.log(data);

            // Use the dynamic data for the chart
            var dynamicData = data.data.prediccion.demanda.data;
            updateChart(dynamicData);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

// Function to update the chart with dynamic data
function updateChart(dynamicData) {
    var dates = dynamicData.map(item => item.fecha);
    var totals = dynamicData.map(item => item.total);

    var datosLineas = {
        labels: dates,
        datasets: [{
            label: 'Demand Prediction',
            data: totals,
            fill: false,
            borderColor: 'blue',
        }],
    };

    // Obtener el elemento canvas
    var ctxLineas = document.getElementById('myChart').getContext('2d');

    // Configuración de los gráficos
    var opciones = {
        responsive: true,
        maintainAspectRatio: false,
    };


    // Create a new chart
    window.myChart = new Chart(ctxLineas, {
        type: 'line',
        data: datosLineas,
        options: opciones,
    });
}