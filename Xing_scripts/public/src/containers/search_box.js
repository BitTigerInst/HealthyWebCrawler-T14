import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchApp } from '../actions/index';
import $ from 'jquery';


export default class SearchBox extends Component{
  constructor(props) {
  	super(props);

  	this.state = {name:'', cate:'', apps:props.apps};
  }


  onInputChange(attr, e) {
    var change = {};
    change[attr] = e.target.value;
    this.setState(change);
  }
  

  onClickEvent(event) {
    event.preventDefault();
    var senddata = $("#form").serialize();
    this.props.fetchApp(senddata);
  }


  render (){
    return (
      <div className="col-md-4">
      	<form id="form" name="form" method = 'get'>
      	    <div className="form-group row">
              <label
                className="col-sm-4 col-form-label"
                htmlFor="app-name">App Name</label>
              <div className="col-sm-8">
        	    	<input
                  id="app-name"
                  className="form-control"
                  type="text" 
                  name="name"
                  value={this.state.name} 
        	        onChange={this.onInputChange.bind(this, 'name')} />
              </div>
      	    </div>
            <div className="form-group row">
              <label
                className="col-sm-4 col-form-label"
                htmlFor="category">Category</label>
              <div className="col-sm-8">
        	      <input
                  id="category"
                  className="form-control"
                  type="text"
                  name="category"
                  value={this.state.cate} 
                  onChange={this.onInputChange.bind(this, 'cate')} />
              </div>
            </div>
      	    <input
              className="btn btn-primary"
              type="submit"
              value = "Submit" 
              onClick={this.onClickEvent.bind(this)} />
      	</form>
      </div>
    );
  }
}

function mapDispatchProps(dispatch) {
  return bindActionCreators({ fetchApp }, dispatch);
}

export default connect(null, mapDispatchProps)(SearchBox);

