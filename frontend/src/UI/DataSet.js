import React from 'react';
import axios from 'axios';

import './DataSet.css'

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
        <div className='insert-data-form'>
          <form onSubmit={this.handleSubmit}>

            <div className='form-group'>
                <label for="insert-description">Description</label>
                <input class="form-control" id="insert-description" type="text" name="description" onChange={this.handleChangeDescription} aria-describedby="description-help"/>
                <small id="description-help" class="form-text text-muted">Describe the expense.</small>
            </div>

            <div className='form-group'>
                <label for="insert-description">Source</label>
                <input class="form-control" id="insert-source" type="text" name="source" onChange={this.handleChangeSource} aria-describedby="source-help"/>
                <small id="source-help" class="form-text text-muted">Enter where this expense was made.</small>
            </div>

            <div className='form-group'>
                <label for="insert-description">Amount</label>
                <input class="form-control" id="insert-amount" type="text" name="amount" onChange={this.handleChangeAmount} aria-describedby="amount-help"/>
                <small id="amount-help" class="form-text text-muted">Enter how much money was used for the expense. e.g. 15.99</small>
            </div>

            <div className='form-group'>
                <label for="insert-description">Date</label>
                <input class="form-control" id="insert-date" type="text" name="date" onChange={this.handleChangeDate} aria-describedby="date-help"/>
                <small id="date-help" class="form-text text-muted">Enter the date when the expense was made in international format. e.g. 2023-01-15</small>
            </div>

            <div className='form-group'>
                <label for="insert-description">Time</label>
                <input class="form-control" id="insert-time" type="text" name="time" onChange={this.handleChangeTime} aria-describedby="time-help"/>
                <small id="time-help" class="form-text text-muted">Enter the time when the expense was made in 24h format. e.g. 14:45</small>
            </div>

            <button className="btn btn-primary text-light" type="submit">Add Expense</button>
          </form>
        </div>
      )
    }
  }

export default DataSet;
