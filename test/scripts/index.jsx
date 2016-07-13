import React from 'react';
import {render} from 'react-dom';
import App from './components/App.jsx'

// import AwesomeComponent from './AwesomeComponent.jsx';

import '../semantic/dist/components/button.min.css';
import '../semantic/dist/components/card.min.css';
import '../semantic/dist/components/container.min.css';
import '../semantic/dist/components/dropdown.min.css';
import '../semantic/dist/components/grid.min.css';
import '../semantic/dist/components/header.min.css';

import '../semantic/dist/components/input.min.css';
import '../semantic/dist/components/message.min.css';
import '../semantic/dist/components/reset.min.css';
import '../semantic/dist/components/search.min.css';
import '../semantic/dist/components/segment.min.css';
import '../semantic/dist/components/site.min.css';
import '../semantic/dist/components/transition.min.css';

render(<App />, document.getElementById('xiaomiapp'));

