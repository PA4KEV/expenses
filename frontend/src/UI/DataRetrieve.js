import React from 'react';
import axios from 'axios';

const DataRetrieve = (props) => {
    const [expense, setPost] = React.useState(null);

    let year = 2023;
    const baseURL = "/get_expenses/year/" + year;

    React.useEffect(() => {
        axios.get(baseURL).then((response) => {
          setPost(response.data);
        });
      }, []);
    
    if (!expense) return( <div><p>Unable to retrieve expense!</p></div>);

    console.log(expense);

    return (
        <div>
            <ul>
                <li>{expense[0].description}</li>
                <li>{expense[0].source}</li>
                <li>{expense[0].amount}</li>
                <li>{expense[0].date}</li>
            </ul>
        </div>
    )
}

export default DataRetrieve;
