import React, { Component } from 'react';
import { connect } from 'react-redux';


class AppList extends Component {

  renderStarApp(rating) {
    console.log(rating);
  }

  renderApp(appData){
    console.log(appData);
    return (
      <div className="app-item col-xxl-2 col-xl-15 col-sm-3 col-xs-4" key={appData._id} >
        <a href={appData._source.appurl}>
          <img className="app-image" src={appData._source.imgurl}></img>
          <h5 className="app-name">{appData._source.title}</h5>
        </a>
        <a href={'http://app.xiaomi.com/category/' + appData._source.cateid}><h6 className="category">{appData._source.category}</h6></a>
        <span className="stars"><span style={{ width: (appData._source.rating * 10) + '%' }}></span></span>
      </div>
    )
  }

  render() {
    return(
      <div className="app-list col-md-8">
        <div className="row">
          {this.props.app.map(this.renderApp)}
        </div>
      </div>
    );
  }
}

function mapStateToProps({app}){
  return { app };
}

export default connect(mapStateToProps)(AppList);