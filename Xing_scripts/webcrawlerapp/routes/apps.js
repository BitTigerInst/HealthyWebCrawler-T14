var express = require('express');
var elasticsearch = require('elasticsearch');
var router = express.Router();

var Apps = require('../models/app');
var elasticClient = new elasticsearch.Client({  
    host: 'localhost:9300',
    log: 'info'
});

/* GET apps listing. */
router.get('/', function(req, res, next) {
  console.log(req.param('name'))
  elasticClient.search({
    "query": { 
       "match": { "title": "微" }
    }
  })
  .then(function(results) {
    console.log(results);
    // res.send(results);
    res.render('apps', {apps: results.hits.hits});
  })
  .catch(function(err) {
    console.log(err);
    res.send(err);
  })
  //res.render('apps', { name: req.param('name') });
});

/* GET apps listing. */
router.post('/', function(req, res, next) {
});

module.exports = router;
