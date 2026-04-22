// static/js/charts.js

function renderCategoryPieChart(labels, values, colors) {
    const ctx = document.getElementById('categoryChart').getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Spending by Category',
                data: values,
                backgroundColor: colors,
                borderColor: '#1e293b',
                borderWidth: 3,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            cutout: '60%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#94a3b8',
                        padding: 16,
                        font: {
                            family: 'Inter',
                            size: 12,
                            weight: '600'
                        },
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    borderColor: '#334155',
                    borderWidth: 1,
                    titleColor: '#f1f5f9',
                    bodyColor: '#94a3b8',
                    padding: 12,
                    callbacks: {
                        label: function(context) {
                            return ' ₹' + context.parsed.toFixed(2);
                        }
                    }
                }
            }
        }
    });
}