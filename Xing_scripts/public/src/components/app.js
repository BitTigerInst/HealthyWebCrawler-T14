import React from 'react';
import { Component } from 'react';

import SearchBox from '../containers/search_box';
import AppList from '../containers/app_list';

export default class App extends Component {
	render() {
		return (
          <div>
            <SearchBox />
            <AppList />
          </div>
		)
	}
}