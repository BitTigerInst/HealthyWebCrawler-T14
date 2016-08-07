export default [
  {
    test: /\.jpg$/,
    loader: 'file-loader?limit=8192&mimetype=image/jpg&name=images/[hash].[ext]'
  },
  {
    test: /\.woff(\?v=\d+\.\d+\.\d+)?$/,
    loader: 'url?limit=8192&mimetype=application/font-woff&name=/[hash].[ext]'
  },
  {
    test: /\.woff2(\?v=\d+\.\d+\.\d+)?$/,
    loader: 'url?limit=8192&mimetype=application/font-woff&name=/[hash].[ext]'
  },
  {
    test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
    loader: 'url?limit=8192&mimetype=application/octet-stream&name=/[hash].[ext]'
  },
  {
    test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
    loader: 'file?limit=8192&mimetype=application/vnd.ms-fontobject&name=/[hash].[ext]'
  },
  {
    test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
    loader: 'url?limit=8192&mimetype=image/svg+xml&name=images/[hash].[ext]'
  }
];
