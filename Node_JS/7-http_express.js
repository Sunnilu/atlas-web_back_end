// Import required modules
const express = require('express');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parse');

// Create the Express app
const app = express();

// Middleware to set the response type to plain text
app.use((req, res, next) => {
  res.setHeader('Content-Type', 'text/plain');
  next();
});

// Handle the root path "/"
app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!\n');
});

// Handle the "/students" path
app.get('/students', (req, res) => {
  const dbPath = path.join(__dirname, process.argv[2]); // Get the CSV file path from command line args

  // Read the CSV file asynchronously
  fs.readFile(dbPath, 'utf-8', (err, data) => {
    if (err) {
      res.status(500).send('Error reading the CSV file\n');
      return;
    }

    // Parse the CSV file
    csv(data, { delimiter: ',' }, (parseErr, output) => {
      if (parseErr) {
        res.status(500).send('Error parsing the CSV file\n');
        return;
      }

      // Filter out invalid students (empty lines or malformed rows)
      const validStudents = output.filter(row => row.length === 2 && row[0].trim() && row[1].trim());

      // Separate students into categories based on course
      const studentsInCS = validStudents.filter(student => student[1].trim() === 'CS');
      const studentsInSWE = validStudents.filter(student => student[1].trim() === 'SWE');

      // Build the response body
      let responseText = 'This is the list of our students:\n';
      responseText += `Number of students: ${validStudents.length}\n`;
      responseText += `Number of students in CS: ${studentsInCS.length}. List: ${studentsInCS.map(student => student[0]).join(', ')}\n`;
      responseText += `Number of students in SWE: ${studentsInSWE.length}. List: ${studentsInSWE.map(student => student[0]).join(', ')}\n`;

      // Send the response
      res.status(200).send(responseText);
    });
  });
});

// Make the app listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the app for testing or further use
module.exports = app;
