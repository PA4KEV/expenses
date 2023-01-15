import React from 'react';

const Expense = (props) => {
    return (
        <div className="card" style={{width: 18 + 'rem'}}>
            <div className="card-body">
                <ul className="list-group" key={props.id}>
                    <li className="list-group-item">{props.description}</li>
                    <li className="list-group-item">{props.amount}</li>
                    <li className="list-group-item">{props.source}</li>
                    <li className="list-group-item">{props.date}</li>
                </ul>
            </div>
        </div>
    )
}

export default Expense;