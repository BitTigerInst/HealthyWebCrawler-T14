/* globals module require __dirname */

var webpack = require('webpack');
var path = require("path");

module.exports = {
  devtool: 'eval',
  entry: [
    'webpack-dev-server/client?http://localhost:8080',
    'webpack/hot/only-dev-server',
    './scripts/index.jsx'
  ],
  output: {
    publicPath: '/assets/',
    path: __dirname + '/build',
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ],
  resolve: {
    extensions: ['', '.js', '.jsx'],
    modulesDirectories: [
      'node_modules',
      'scripts'
    ]
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loaders: ['react-hot', 'babel'],
        exclude: /node_modules/
      },
      {
        test: /\.jsx?/,
        loaders: ['react-hot', 'babel'],
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: 'style!css',
        exclude: /node_modules/
      },
      {
        test: /\.(woff|woff2|ttf|svg)$/,
        loader: 'url?limit=100000',
        exclude: /node_modules/
      },
      {
        test: /\.(eot|png)$/,
        loader: 'file',
        exclude: /node_modules/
      }
    ]
  }
};
