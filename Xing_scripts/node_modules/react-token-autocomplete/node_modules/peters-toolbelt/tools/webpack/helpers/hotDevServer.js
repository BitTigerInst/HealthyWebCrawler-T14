import _ from 'lodash';

export default function(conf) {
  if (process.env.NODE_ENV === 'production') {
    return conf;
  } else {
    conf.entry = _.isArray(conf.entry) ? conf.entry : [conf.entry];
    conf.entry.unshift('webpack/hot/dev-server');
    return conf;
  }
}
