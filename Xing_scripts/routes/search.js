var express = require('express');
var elasticsearch = require('elasticsearch');
var router = express.Router();

var Apps = require('../models/app');

var client = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});

var index = "scrapy";
var type = "xiaomiapp";

router.get('/', function(req, res, next) {
  var data = req.query;

  var name = data['name'] || "";
  var cate = data['category'] || "";

  Apps.search({
	    query: {
        bool: {
          should: [
            { match: { title: name}},
            { match: { category: cate}}
          ]
        }        
	    }
  },
  function(err, results) {
    if (err) {
      console.log(err);
    }
    res.send(200, JSON.stringify(results.hits.hits));
  });
});

module.exports = router;