import React from 'react';
import MyComponent from '../pages/index'; // Import the MyComponent

const App: React.FC = () => {
  return (
    <div>
      <h1>My App</h1>
      <MyComponent /> {/* Render the MyComponent */}
    </div>
  );
};

export default App;