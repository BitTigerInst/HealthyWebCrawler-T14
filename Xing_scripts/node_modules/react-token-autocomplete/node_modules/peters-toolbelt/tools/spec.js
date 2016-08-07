import toolbelt from './';
import {expect} from 'chai';

describe('toolbelt', () => {
  it('exports', () => {
    expect(toolbelt.webpack).to.exist;
  });
});
