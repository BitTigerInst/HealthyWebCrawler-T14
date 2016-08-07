'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});
exports['default'] = [{
  test: /bootstrap\/js\//,
  loader: 'imports?jQuery=jquery'
}, {
  test: /\.png$/,
  loader: 'url-loader?limit=8192&mimetype=image/png&name=images/[hash].[ext]'
}];
module.exports = exports['default'];