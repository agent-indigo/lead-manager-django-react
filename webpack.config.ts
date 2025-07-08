import {Configuration} from 'webpack'
const webpackConfig: Configuration = {
  module: {
    rules: [{
      test: /\.tsx?$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader'
      }
    }]
  }
}
export default webpackConfig