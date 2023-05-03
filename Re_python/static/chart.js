document.addEventListener('DOMContentLoaded', function () {
    // Retrieve the ticket status data from the server
    fetch('/ticket_status_data')
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        // Prepare the chart data
        var chartData = {
          labels: Object.keys(data),
          datasets: [
            {
              data: Object.values(data),
              backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
                'rgba(255, 159, 64, 0.6)'
              ]
            }
          ]
        };
  
        // Create the chart
        var ctx = document.getElementById('ticketStatusChart').getContext('2d');
        var ticketStatusChart = new Chart(ctx, {
          type: 'pie',
          data: chartData
        });
      })
      .catch(function (error) {
        console.log('Error:', error);
      });
  });
  