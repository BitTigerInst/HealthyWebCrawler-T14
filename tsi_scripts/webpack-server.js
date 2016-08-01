// import webpack from 'webpack';
// import WebpackDevServer from 'webpack-dev-server';
// import config from './webpack.config';

webpack = require('webpack');
WebpackDevServer = require('webpack-dev-server');
config = require('./webpack.config');

const port = 8080  host = 'localhost';

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  stats: {
    colors: true
  },
  historyApiFallback: true
}).listen(port, host, function (err, result) {
  if (err) {
    console.log(err);
  }

  console.log(`Listening at ${host}:${port}`);
});
