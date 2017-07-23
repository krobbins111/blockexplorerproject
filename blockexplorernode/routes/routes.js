module.exports = function (app) {
    app.get('/', function(req, res, next) {
        res.render('index', { title: 'Chart' });
    });

    app.post('/stockData', function (req, res) {
        if(req.body.query) {
            res.send(true);
            
        }else {
            res.send(false)
        }
    });
}