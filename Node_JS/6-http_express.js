// Import the Express module
const express = require('express');

// Initialize the Express app
const app = express();

// Define the root route ("/")
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the app listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the app to be used elsewhere (e.g., for testing purposes)
module.exports = app;
