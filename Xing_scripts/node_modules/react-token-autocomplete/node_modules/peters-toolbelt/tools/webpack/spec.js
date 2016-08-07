import WebpackConfig from './';
import {expect} from 'chai';

describe('webpack', () => {
  it('exists', () => {
    expect(WebpackConfig).to.exist;
  });
});
