import React from 'react';
import {render} from 'react-dom';
import $ from 'jquery';
import emitter from '../emitter';

// import '../vendor/dropdown';
// import 'semantic-ui-transition/transition.css'
// import {Icon} from 'react-native-vector-icons/FontAwesome'

class Header extends React.Component {
  // getInitialState: function() {
  //  return {query: 'Hello!'};
  // },

  componentDidMount() {
    // $('.menu.dropdown').dropdown();
    // this.state = {
    //  query : '0'
    // }
  }

  componentWillUnmount() {
    // reset dropdown
    // $('.ui.dropdown').dropdown('refresh');
  }

  _onChange = (e) => {
    this.setState({query: e.target.value});
  }
  
  _search = (e) => {
    // only trigger search while user type enter
    e.keyCode === 13 && emitter.emit('search', this.state);
  };

  render() {
    return (
       <div className="ui inverted vertical segment center aligned">
        <div className="ui right action left icon input massive">
          <i className="search icon"></i>
          <input
            type="text"
            onKeyDown={this._search}
            onChange={this._onChange}
            placeholder="Search..."
            autoFocus
          />          
          <div className="ui dropdown button" tabindex="0">
	    <div className="text">All</div>
            <i className="dropdown icon"></i>
	    <div className="menu transition" tabindex="-1">
              <div className="item">All</div>
              <div className="item">Audiobook</div>
              <div className="item">eBook</div>
              <div className="item">Movie</div>
              <div className="item">Music</div>
              <div className="item">Music Video</div>
              <div className="item">Podcast</div>
              <div className="item">TV Show</div>
              <div className="item">Short Film</div>
              <div className="item">Software</div>
            </div>
	  </div>
        </div>
      </div>
	  );
  }
}

export default Header;
