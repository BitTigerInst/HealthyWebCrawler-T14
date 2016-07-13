import React from 'react';
import {render} from 'react-dom';
import axios from 'axios';
import $ from 'jquery';

import emitter from '../emitter';
import Map from './Map';
// import reqwest from 'reqwest';

class Container extends React.Component {
  

  componentDidMount = () => {
    // const d = 2;
    this.state = {count: '', results: ''};
    emitter.on('search', (state) => {
      this.setState({ count: '0' });
      // const url = 'http://localhost:3000/search?name='.concat("",d);
      const url = 'http://localhost:3000/search?name='.concat("", state.query);
      axios.get(url)
      .then(response => this.setState({ count: response.data.hits.total, results: response.data.hits.hits }))
      .fail(err => this.setState({ count: '-1' }));
    }); 
  };      

  componentWillUnmount = () => {
    emitter.removeListener('search');
  };
  
  loadRender () {
    
    // const d = 3;
    // return <img src={this.state.results.hits[0]._source.image} /> 
    const {count, results } = this.state;
    const res = { count, results };
    
    if (!this.state.results) {
      return <div>Loading... </div>;
    }

    // return <img src={results.hits[0]._source.image} />
    // return <p> {this.state.count} </p>
    // return <p> {res.count} </p>
    return (<Map {...res} />);
  }

  render() {
    return (
      <div
        style={{
          margin: '50px auto',
          maxWidth: '900px'
        }}
      >
        {this.loadRender()}
      </div>
    );
  }

}

export default Container;

