import fs from 'fs';
import path from 'path';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(path.resolve(filePath), 'utf-8', (err, data) => {
      if (err) {
        return reject(err);
      }

      // Assuming the CSV format is:
      // firstname, major, field
      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = {};

      lines.forEach(line => {
        const [firstname, major, field] = line.split(',');
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      });

      resolve(students);
    });
  });
};
