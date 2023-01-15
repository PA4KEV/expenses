import React from 'react';
import axios from 'axios';


class DataSet extends React.Component {
    state = {
      description: '',
      source: '',
      amount: '',
      date: '',
      time: ''
    }
  
    handleChangeDescription = event => {
        console.log("Handle change description");
        this.setState({
            description: event.target.value
        });
    }
    handleChangeSource = event => {
        console.log("Handle change source");
        this.setState({
            source: event.target.value
        });
    }
    handleChangeAmount = event => {
        console.log("Handle change amount");
        this.setState({
            amount: event.target.value
        });
    }
    handleChangeDate = event => {
        console.log("Handle change date");
        this.setState({
            date: event.target.value
        });
    }
    handleChangeTime = event => {
        console.log("Handle change time");
        this.setState({
            time: event.target.value
        });
    }
  
    handleSubmit = event => {
        event.preventDefault(); // Halt default form behaviour.

        console.log("Handle submit");

        const baseURL = "http://localhost:8050/insert_new_expense";
  
        const expense = {
            description: this.state.description,
            source: this.state.source,
            amount: parseFloat(this.state.amount),
            date: this.state.date,
            time: this.state.time
        };

        console.log(expense);
  
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
              Description:
              <input type="text" name="description" onChange={this.handleChangeDescription}/>
            </label>
            <br/>
            <label>
              Source:
              <input type="text" name="source" onChange={this.handleChangeSource}/>
            </label>
            <br/>
            <label>
              Amount:
              <input type="text" name="amount" onChange={this.handleChangeAmount}/>
            </label>
            <br/>
            <label>
              Date:
              <input type="text" name="date" onChange={this.handleChangeDate}/>
            </label>
            <br/>
            <label>
              Time:
              <input type="text" name="time" onChange={this.handleChangeTime}/>
            </label>
            <br/>
            <button type="submit">Add Expense</button>
          </form>
        </div>
      )
    }
  }

export default DataSet;
