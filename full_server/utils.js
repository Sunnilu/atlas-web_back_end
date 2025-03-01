import fs from 'fs';
import path from 'path';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(path.resolve(filePath), 'utf-8', (err, data) => {
      if (err) {
        return reject(err); // Reject if the file can't be read
      }

      // Split data by lines and filter out empty lines
      const lines = data.split('\n').filter(line => line.trim() !== '');
      const studentsByField = {};

      // Process each line (skip the first line if it's a header)
      lines.forEach(line => {
        const [firstname, major, field] = line.split(',').map(str => str.trim());

        // Skip lines that don't have enough data
        if (!firstname || !major || !field) return;

        // Ensure the field exists in the studentsByField object
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }

        // Add the student's first name to the corresponding field array
        studentsByField[field].push(firstname);
      });

      // Resolve the promise with the data object
      resolve(studentsByField);
    });
  });
};

