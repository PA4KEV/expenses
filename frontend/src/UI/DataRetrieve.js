import React from 'react';
import axios from 'axios';
import Expense from '../expenses/Expense';

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
                <Expense
                description={expense.description}
                source={expense.source}
                amount={expense.amount}
                date={expense.date}
                />
              )
          }
        </div>
      )
    }
  }

export default DataRetrieve;
