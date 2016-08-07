'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});
exports['default'] = [{
  test: /\.scss$/,
  loader: 'style!css!sass'
}, {
  test: /\.css$/,
  loader: 'style!css'
}];
module.exports = exports['default'];