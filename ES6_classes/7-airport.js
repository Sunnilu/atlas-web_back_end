export default class Airport {
  constructor(name, code) {
    this._name = this._validateName(name);
    this._code = this._validateCode(code);
  }

  // Getter for name
  get name() {
    return this._name;
  }

  // Getter for code
  get code() {
    return this._code;
  }

  // String representation of the class
  toString() {
    return this._code;
  }

  // Validation methods
  // eslint-disable-next-line class-methods-use-this
  _validateName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    return name;
  }

  // eslint-disable-next-line class-methods-use-this
  _validateCode(code) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    return code;
  }
}
