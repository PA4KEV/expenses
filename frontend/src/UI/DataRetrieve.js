import React from 'react';
import axios from 'axios';



class DataRetrieve extends React.Component {
    state = {
      expenses: []
    }

    componentDidMount() {
        let year = 2023;
        const baseURL = "http://localhost:8050/get_expenses/year/" + year;

        axios.get(baseURL)
            .then(res => {
                const expenses = res.data;
                this.setState({ expenses });
            })
    }

    render() {
      return (
        <div>
          {
            this.state.expenses
              .map(expense =>
                <ul key={expense.id}>
                    <li>{expense.description}</li>
                    <li>{expense.amount}</li>
                    <li>{expense.source}</li>
                    <li>{expense.date}</li>
                </ul>
              )
          }
        </div>
      )
    }
  }

export default DataRetrieve;
