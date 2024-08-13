import React, { useState, useEffect } from 'react';
import axios from 'axios';


const MyComponent = () => {
  const [data, setData] = useState();

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching data from API...');
        const response = await axios.get('http://localhost:8000/player');
        console.log('Received data:', response.data);
        setData(response.data['name']);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
        <h1>My Component</h1>
        <div>
            Hello {data} !
        </div>
    </div>
  );
};

export default MyComponent;