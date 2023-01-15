import React from 'react';
import axios from 'axios';

async function connectionTest() {
    try{
        const response = await axios.get('/connection_test');
        console.log('response  ', response)
        return response.data;
    } catch(error) {
        return [];
    }    
}

async function getExpenses() {
    try{
        const response = await axios.get('/get_expenses/year/2023');
        console.log('response  ', response)
        return response.data;
    } catch(error) {
        return [];
    }    
}


const DataRetrieve = (props) => {
    

    connectionTest();
    getExpenses();

    return (
        <div>Test</div>
    )
}

export default DataRetrieve;
