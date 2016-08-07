import loaders from './loaders';
import helpers from './helpers';
import _ from 'lodash';

class WebpackConf {

    constructor(config) {
      this.userConfig = config;
      this._config = _.clone(this.config);
    }

    config = {
      output: {
        path: 'dist',
        filename: 'bundle.js'
      },
      module: {
        loaders: []
      },
      resolve: {
        alias: {},
        extensions: []
      },
      node: {
        net: 'empty',
        tls: 'empty',
        dns: 'empty',
        fs: 'empty'
      },
      plugins: []
    }

    postProcess = []

    addLoaders(loaders) {
      this.config.module.loaders = this.config.module.loaders.concat(loaders);
      return this;
    }

    addPlugins(plugins) {
      this.config.plugins = this.config.plugins.concat(plugins);
      return this;
    }

    addExtensions(extensions) {
      extensions = _.isArray(extensions) ? extensions : [extensions];
      this._config.resolve.extensions = this._config.resolve.extensions.concat(extensions);
    }

    iNeedES7() {
      return this.addLoaders(loaders.ES7);
    }

    iNeedSCSS() {
      return this.addLoaders(loaders.SCSS);
    }

    iNeedReact() {
      this.addExtensions(['', '.jsx', '.js']);
      return this.addLoaders(loaders.reactES7);
    }

    iNeedWebFonts() {
      return this.addLoaders(loaders.webfonts);
    }

    iNeedBootstrap() {
      this.iNeedWebFonts();
      return this.addLoaders(loaders.bootstrap);
    }

    iNeedImages() {
      return this.addLoaders(loaders.images);
    }

    iNeedInlineSVGs() {
      return this.addLoaders(loaders.inlineSVG);
    }

    iNeedHotDevServer() {
      this.postProcess.push(helpers.hotDevServer);
      return this;
    }

    getConfig() {
      let conf = _.merge(this.config, this.userConfig, this._config);

      _.each(this.postProcess, helper => {
        conf = helper(conf);
      });

      return conf;
    }

}

export default WebpackConf;
