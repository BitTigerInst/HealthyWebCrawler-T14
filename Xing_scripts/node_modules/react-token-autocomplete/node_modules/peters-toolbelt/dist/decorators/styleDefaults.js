'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _lodash = require('lodash');

exports['default'] = function () {
  var styles = arguments.length <= 0 || arguments[0] === undefined ? {} : arguments[0];

  return function (Component) {
    Component.defaultProps = (0, _lodash.extend)({}, { style: styles }, Component.defaultProps);
    return Component;
  };
};

module.exports = exports['default'];