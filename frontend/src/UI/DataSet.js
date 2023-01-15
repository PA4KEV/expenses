import React from 'react';
import axios from 'axios';


// const DataSet = (props) => {
//     const [setExpense] = React.useState(null);

//     function insertExpense() {
//         const baseURL = "/insert_new_expense/";

//         axios
//           .post(baseURL, {
//             description: "Razor Crest",
//             source: "LEGO",
//             amount: 139.99,
//             date: "2023-01-15",
//             time: "14:00"
//           })
//           .then((response) => {
//             setExpense(response.data);
//           });
//     }

//     return (
//         <div>
//             <button onClick={insertExpense}>Create Expense</button>
//         </div>
//     )
// }

class DataSet extends React.Component {
    state = {
      name: ''
    }
  
    handleChange = event => {
      this.setState({ name: event.target.value });
    }
  
    handleSubmit = event => {
        const baseURL = "http://localhost:8050/insert_new_expense";
        event.preventDefault();
  
        const expense = {
            description: this.state.name,
            source: "TEST",
            amount: 139.99,
            date: "2023-01-15",
            time: "14:55"
        };
  
        axios.post(baseURL, { expense })
        .then(res => {
            console.log(res);
            console.log(res.data);
        })
    }
  
    render() {
      return (
        <div>
          <form onSubmit={this.handleSubmit}>
            <label>
              Expense:
              <input type="text" name="name" onChange={this.handleChange} />
            </label>
            <button type="submit">Add Expense</button>
          </form>
        </div>
      )
    }
  }
  


export default DataSet;
