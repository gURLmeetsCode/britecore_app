const path = require('path');
const webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');


module.exports = {
  entry: './client/src/index',
  module: {
    rules: [
      /* JS */
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      /* SCSS */
      {
        test: /\.scss?$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              config: {
                  path: './client/config/postcss.config.js'
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      }
    ]
  },
  output: {
    filename: '[name]-[hash].js',
    path: path.resolve(__dirname, './client/static/bundles/')
  },
  devServer: {
    contentBase: './client/src',
    hot: true,
    historyApiFallback: true
  },
  resolve: {
   extensions: ['.js', '.jsx','.scss']
 },
  plugins: [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin('style.css')
  ]
}
