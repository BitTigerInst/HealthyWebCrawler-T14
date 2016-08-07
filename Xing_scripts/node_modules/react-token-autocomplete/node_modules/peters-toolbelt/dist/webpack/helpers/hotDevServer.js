'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

var _lodash = require('lodash');

var _lodash2 = _interopRequireDefault(_lodash);

exports['default'] = function (conf) {
  if (process.env.NODE_ENV === 'production') {
    return conf;
  } else {
    conf.entry = _lodash2['default'].isArray(conf.entry) ? conf.entry : [conf.entry];
    conf.entry.unshift('webpack/hot/dev-server');
    return conf;
  }
};

module.exports = exports['default'];