var router = require('./routes/route');
var app = require('express')();

app.use('/', router);
app.listen(3000);

console.log('Magic');
