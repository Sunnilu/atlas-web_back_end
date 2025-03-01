const http = require('http');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parse');

// Create the HTTP server
const app = http.createServer((req, res) => {
  const { url } = req;

  // Set response header for plain text
  res.setHeader('Content-Type', 'text/plain');

  // Handle the root path "/"
  if (url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!\n');
  }
  // Handle the "/students" path
  else if (url.startsWith('/students')) {
    const dbPath = path.join(__dirname, process.argv[2]); // Get the CSV path from the command line args
    fs.readFile(dbPath, 'utf-8', (err, data) => {
      if (err) {
        res.statusCode = 500;
        res.end('Error reading the CSV file\n');
        return;
      }

      // Parse the CSV file
      csv(data, { delimiter: ',' }, (parseErr, output) => {
        if (parseErr) {
          res.statusCode = 500;
          res.end('Error parsing the CSV file\n');
          return;
        }

        // Filter out invalid students (empty lines)
        const validStudents = output.filter(row => row.length > 1 && row[0].trim() && row[1].trim());

        // Build the response body
        let responseText = 'This is the list of our students:\n';
        validStudents.forEach(student => {
          responseText += `Name: ${student[0]}, Age: ${student[1]}\n`;
        });

        // Send the response
        res.statusCode = 200;
        res.end(responseText);
      });
    });
  } else {
    // Handle other paths (404)
    res.statusCode = 404;
    res.end('Not Found\n');
  }
});

// Make the app exportable
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
