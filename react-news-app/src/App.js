import './App.css';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './containers/HomePage';

function App() {
  return (
    <div >
      <Router>
        <div>
          <Switch>
            <Route exact path="/" component={HomePage} />
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
