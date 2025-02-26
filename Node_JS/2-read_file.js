const fs = require('fs');

function countStudents(path) {
  try {
    // Read the database file synchronously
    const data = fs.readFileSync(path, 'utf-8');
    
    // Split the file by lines and filter out empty lines
    const lines = data.trim().split('\n').filter(line => line !== '');
    
    // Check if there are no students (only the header)
    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    // Extract the field names (the first line in the file)
    const fields = lines[0].split(',');

    // Create a map to count students in each field
    const studentsByField = {};

    // Iterate through each line of data (skip header line)
    for (let i = 1; i < lines.length; i++) {
      const values = lines[i].split(',');
      // Iterate over the fields to organize students by each field
      fields.forEach((field, index) => {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(values[index]);
      });
    }

    // Count total students (excluding header and empty lines)
    const numberOfStudents = lines.length - 1;

    // Log the total number of students
    console.log(`Number of students: ${numberOfStudents}`);
    
    // Log the number of students in each field and the list of first names
    fields.forEach(field => {
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
    });
  } catch (error) {
    // Handle errors (e.g., file not found)
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
