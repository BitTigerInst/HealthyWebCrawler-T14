import React from 'react';
import {render} from 'react-dom';
import $ from 'jquery';
import emitter from '../emitter';

import '../vendor/dropdown';
import '../vendor/transition';
// import 'semantic-ui-transition/transition.css'
// import {Icon} from 'react-native-vector-icons/FontAwesome'

class Header extends React.Component {
  // getInitialState: function() {
  //  return {query: 'Hello!'};
  // },

  componentDidMount() {
    this.state = {
      category: 'all'
    };

    // const self = this;
    // initialize semantic UI dropdown
    $('.ui.dropdown').dropdown(
      {
        // onShow: function(){},
        // onHide: function(){}
        // onChange: (val) => { this.changeHandler(val).bind(this) }, this
        onChange: (val) => {this.onClick(val)}
      }
    );

    // console.log(this.state.category);
    // $('.menu.dropdown').dropdown();
    // this.state = {
    //  query : '0'
    // }
  }

  compinentWillMount() {
    $('.ui.dropdown').dropdown(
      {
        onHide: function(){}
      }
    );
  }

  componentWillUnmount() {
    // reset dropdown
    $('.ui.dropdown').dropdown('refresh');
  }

  onClick = (value) => {
    this.setState({ category: value });
    // console.log(this.state.category);
    // only start search if there is a search query inside of input box
    this.state.query && emitter.emit('search', this.state);
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
          <div className="ui floating dropdown icon button" tabindex="0">
	    <div className="text"> <p>  All  </p> </div>
            <div className="add blank space"> <i className="dropdown icon"></i> </div>
	    <div className="menu transition" tabindex="-1">
              <div className="item">All</div>
              <div className="item">实用工具</div>
              <div className="item">聊天社交</div>
              <div className="item">学习教育</div>
              <div className="item">时尚购物</div>
              <div className="item">旅行交通</div>
              <div className="item">医疗健康</div>
              <div className="item">新闻资讯</div>
              <div className="item">金融理财</div>
              <div className="item">影视视听</div>
	      <div className="item">图书阅读</div>
	      <div className="item">效率办公</div>
	      <div className="item">居家生活</div>
	      <div className="item">摄影摄像</div>
 	      <div className="item">体育运动</div>
	      <div className="item">娱乐消遣</div>
            </div>
	  </div>
        </div>
      </div>
	  );
  }
}

export default Header;
