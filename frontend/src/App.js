import './overrides.scss';
import "bootstrap/dist/js/bootstrap.bundle.min";

import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import './App.css';

import DataRetrieve from './UI/DataRetrieve';
import DataSet from './UI/DataSet';
import Navigation from './UI/Navigation';


function App() {
  return (
    <div className="app container-md">
      <Router>
        <Navigation/>

        <Routes>
            <Route exact path='/get_expenses' element={<DataRetrieve />}></Route>
            <Route exact path='/set_expenses' element={<DataSet />}></Route>
        </Routes>
        </Router>
    </div>
  );
}

export default App;
