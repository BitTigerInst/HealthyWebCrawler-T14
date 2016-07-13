import React, { PropTypes } from 'react';
import Item from './Items';

const Map = (res) => (
  <div className="ui link cards">
    { res.count > 0 ? res.results.map((item) => <Item {...item} key={item._id} />) : res.count }
  </div>
);

Map.propTypes = {
  count: PropTypes.number,
  results: PropTypes.array
};

export default Map;
