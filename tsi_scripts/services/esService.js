var elasticsearch = require('elasticsearch');

var client = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});

var index = "scrapy";
var type = "xiaomiapp";

function performSearch(name, category) {
    if (category == "all") {
        return client.search({
            index: 'scrapy',
            type: 'xiaomiapp',
            body: {
                query: {
                  match: {
                     _all: name
                  }
                }
            }
        })
 
    }

    return client.search({
	index: 'scrapy',
	type: 'xiaomiapp',
	body: {
	    query: {
	      "bool": {
                "must": [
                  { "match": { "title": name}},
                  { "match": { "category": category}}
                ]
              }
	    }
        }
    })
//.then(function (resp) {
//	var hits = resp.hits.hits;
//    }, function (err) {
//	console.trace(err.message);
//    })
}

exports.performSearch = performSearch;
