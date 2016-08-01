var express = require('express');
var router = express.Router();
var elastic = require('../services/esService');

router.get("/search", function (req, res, next) {
    // elastic.performSearch(req.query.name).then(function(result) {res.jsonp(result)});
    // console.log("name=" + req.query.name);


    var values = req.query.name.split(" ")
    // elastic.performSearch(values[0], values[1]).then(function(result) {res.jsonp(result)});
    elastic.performSearch.apply(this, values).then(function(result) {res.jsonp(result)});
    console.log(values[1])
})

module.exports = router;
