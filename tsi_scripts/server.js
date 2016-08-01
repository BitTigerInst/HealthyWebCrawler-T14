var router = require('./routes/route');
var app = require('express')();

app.all(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods: PUT, GET, POST");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

var cors = require('cors');
app.use(cors());

app.use('/', router);
app.listen(3000);

console.log('Magic');
