
      // Nueva solicitud dentro del bloque then de la primera solicitud
    /*  fetch('http://144.22.133.47:8000/api/factura')
        .then(response => response.json())
        .then(data => {
          // Reemplaza ... con tus propios datos
          var fechas  = data.facturas.map(factura => {
      const fecha = new Date(factura.fecha);
      const year = fecha.getFullYear();
      const month = String(fecha.getMonth() + 1).padStart(2, '0'); // Se suma 1 ya que los meses son base 0
      const day = String(fecha.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    });
          var ventasReales = data.facturas.map(factura => factura.total); // Puedes ajustar esto según la estructura de tus datos
          var demandasPronosticadas = data.facturas.map(factura => factura.total);;
          // Resto del código para el gráfico de Ventas Reales y Demanda Pronosticada
          var datosLinealVentas = {
            labels: fechas,
            datasets: [
              {
                label: 'Ventas Reales',
                data: ventasReales,
                fill: false,
                borderColor: 'rgba(75, 192, 192, 1)',
              },
              {
                label: 'Demanda Pronosticada',
                data: demandasPronosticadas,
                fill: false,
                borderColor: 'rgba(255, 99, 132, 1)',
              },
            ],
          };

          // Inicialización del segundo gráfico de línea
          var ctxLinealVentas = document.getElementById('graficoLinealVentas').getContext('2d');
          new Chart(ctxLinealVentas, {
            type: 'line',
            data: datosLinealVentas,
            options: {
              responsive: true,
              maintainAspectRatio: false,
            },
          });
        })
        .catch(error => console.error('Error al obtener datos:', error));*/
