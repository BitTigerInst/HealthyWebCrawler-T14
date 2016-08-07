import {extend} from 'lodash';

export default function(styles = {}) {
  return function (Component) {
    Component.defaultProps = extend({}, {style: styles}, Component.defaultProps);
    return Component;
  };
}
