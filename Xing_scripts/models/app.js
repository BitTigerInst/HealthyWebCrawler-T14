var mongoose = require('mongoose');
var mongoosastic = require('mongoosastic');
var Schema = mongoose.Schema;

var AppSchema = new Schema({
  category: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  rating: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  appurl: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  version: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  title: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  developerrec: {
    type: [String],
    es_indexed: true,
    es_type: 'nested'
  },
  relatedrec: {
    type: [String],
    es_indexed: true,
    es_type: 'nested'
  },
  imgurl: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  appid: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  updatetm: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  cateid: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  ratingct: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  },
  developer: {
    type: String,
    es_indexed: true,
    es_type: 'string'
  }
},
 { collection : 'xiaomiapp' }
);

AppSchema.plugin(mongoosastic, {index: 'scrapy'});

var AppsModel = mongoose.model('xiaomiapp', AppSchema)
  , stream = AppsModel.synchronize()
  , count = 0;

AppsModel.createMapping(function(err, mapping){  
  if(err){
    console.log('error creating mapping (you can safely ignore this)');
    console.log(err);
  }else{
    console.log('AppsModel mapping created!');
    console.log(mapping);
  }
});

stream.on('data', function(err, doc){
  count++;
});
stream.on('close', function(){
  console.log('indexed ' + count + ' documents!');
});
stream.on('error', function(err){
  console.log(err);
});

module.exports = AppsModel;