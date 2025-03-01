import { readDatabase } from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('./database.csv');
      let response = 'This is the list of our students\n';

      const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      fields.forEach(field => {
        const studentNames = students[field];
        response += `Number of students in ${field}: ${studentNames.length}. List: ${studentNames.join(', ')}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase('./database.csv');
      const filteredStudents = [];

      Object.keys(students).forEach(field => {
        filteredStudents.push(...students[field].filter(firstname => firstname.includes(major)));
      });

      res.status(200).send(`List: ${filteredStudents.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
