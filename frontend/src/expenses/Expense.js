import React from 'react';

const Expense = (props) => {
    return (
        <tr>
            <td>{props.description}</td>
            <td>{props.amount}</td>
            <td>{props.source}</td>
            <td>{props.date}</td>
        </tr>
    )
}

export default Expense;