import './overrides.scss';
import "bootstrap/dist/js/bootstrap.bundle.min";

import './App.css';
import DataRetrieve from './UI/DataRetrieve';
import DataSet from './UI/DataSet';

function App() {
  return (
    <div className="App">
      <h1 className="text-primary">Expenses</h1>
      <DataSet/>
      <DataRetrieve/>
    </div>
  );
}

export default App;
