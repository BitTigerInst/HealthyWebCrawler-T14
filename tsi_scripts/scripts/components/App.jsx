import React from 'react';
import {render} from 'react-dom';
import Header from './Header';
import Container from './Container';

//const App = () => {

class App extends React.Component {
  render () {
    return (
      <div>
        <Header />
        <Container />
      </div>
    );
  }
};

export default App;
