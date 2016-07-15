import React, { PropTypes } from 'react';
import moment from 'moment';

const Item = (result) => (
  <a className="ui card" href={result._source.appurl} target="_blank">
    <div className="image">
      <img alt="img" src={result._source.image} />
    </div>
    <div className="content">
      <div className="header">{result._source.title}</div>
      <div className="meta right floated">
        {result._source.category}
      </div>
      <div className="meta">
        {result._source.developer}
      </div>
      <div>
      </div>
      <br />
      <div className="rating info">
        <span className="rating right floated">
          Count {result._source.ratingct}
        </span>
        <span className="rating">
          Rating {result._source.rating}
        </span>
      </div>
    </div>
    <div className="extra content">
      <div className="meta-1">
        <span className="detail right floated">
          Release on {moment(result._source.updatetm).format('MMM DD, YYYY')}
        </span>
        <span className="detail">
          Version {result._source.version}
        </span>
      </div>
    </div>
    <div className="developer application">
      {result._source.developerrec.length == 0 ?
        <br /> : <span>
          <i className="search icon"></i>
          {result._source.developerrec.join(' ')}
        </span> 
      }
    </div>
    <div className="related application">
      {result._source.relatedrec.length == 0 ?
        <br /> : <span>
          <i className="search icon"></i>
          {result._source.relatedrec.join(' ')}
        </span> 
      }
    </div>
  </a>
);

export default Item;
