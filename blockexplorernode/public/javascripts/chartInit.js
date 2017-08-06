$(document).ready(function () {
    google.charts.load('current', {'packages':['line']});

    function drawChart(dataPoints) {

        var data = new google.visualization.DataTable();
        data.addColumn('number', 'Day');
        data.addColumn('number', 'DOW JONES Index');
        data.addColumn('number', 'S&P 500 Index');
        data.addColumn('number', 'Bitcoin');

        data.addRows(dataPoints);

        var options = {
            chart: {
                title: 'Index vs Bitcoin',
            },
            width: 900,
            height: 500
        };

        console.log($('#linechart_material'));

        var chart = new google.charts.Line(document.getElementById('linechart_material'));

        chart.draw(data, google.charts.Line.convertOptions(options));
    }
});