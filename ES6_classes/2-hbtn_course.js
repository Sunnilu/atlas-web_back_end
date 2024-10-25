/* eslint-disable class-methods-use-this */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateName(name);
    this._length = this._validateLength(length);
    this._students = this._validateStudents(students);
  }

  // Name getter
  get name() {
    return this._name;
  }

  // Name setter
  set name(value) {
    this._name = this._validateName(value);
  }

  // Length getter
  get length() {
    return this._length;
  }

  // Length setter
  set length(value) {
    this._length = this._validateLength(value);
  }

  // Students getter
  get students() {
    return this._students;
  }

  // Students setter
  set students(value) {
    this._students = this._validateStudents(value);
  }

  // Validation methods
  // eslint-disable-next-line class-methods-use-this
  _validateName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    return name;
  }

  // eslint-disable-next-line class-methods-use-this
  _validateLength(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    return length;
  }

  _validateStudents(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    return students;
  }
}
