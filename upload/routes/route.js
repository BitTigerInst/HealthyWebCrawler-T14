var express = require('express');
var router = express.Router();
var elastic = require('../services/esService');

router.get("/search", function (req, res, next) {
    elastic.performSearch(req.query.name).then(function(result) {res.json(result)});
    console.log("name=" + req.query.name);
})

module.exports = router;
