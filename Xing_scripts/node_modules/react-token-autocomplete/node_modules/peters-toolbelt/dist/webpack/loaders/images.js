'use strict';

Object.defineProperty(exports, '__esModule', {
    value: true
});
exports['default'] = [{
    test: /\.(jpe?g|png|gif|svg)$/i,
    loaders: ['file?hash=sha512&digest=hex&name=[hash].[ext]', 'image-webpack?bypassOnDebug&optimizationLevel=7&interlaced=false']
}];
module.exports = exports['default'];