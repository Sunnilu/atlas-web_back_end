const fs = require('fs');

function countStudents(path) {
  // Read the file asynchronously
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) {
      // Handle the error if the file cannot be read
      throw new Error('Cannot load the database');
    }

    // Split the file content into lines and filter out empty lines
    const lines = data.trim().split('\n').filter(line => line !== '');

    // If there are no students (only the header), throw an error
    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    // Extract the field names from the first line (header)
    const fields = lines[0].split(',');

    // Create an object to hold students categorized by field
    const studentsByField = {};

    // Loop through each line (excluding header) to process student data
    for (let i = 1; i < lines.length; i++) {
      const values = lines[i].split(',');

      // Loop through each field to categorize students by field
      fields.forEach((field, index) => {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(values[index]);
      });
    }

    // Count the total number of students (excluding header)
    const numberOfStudents = lines.length - 1;

    // Output the number of students
    console.log(`Number of students: ${numberOfStudents}`);

    // Output the number of students per field and list their names
    fields.forEach(field => {
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
    });
  });
}

module.exports = countStudents;
