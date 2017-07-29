$(document).ready(function () {
    google.charts.load('current', {'packages':['line']});
    google.charts.setOnLoadCallback(initSocket);

});

function initSocket() {
    var socket = io.connect('http://10.0.0.141:3000');

    socket.on('stockData', function (data) {
        drawChart(data);
    });
}

function drawChart(dataPoints) {

    dataPoints = [
        [1,5,7,8],
        [2,6,7,9]
    ]

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