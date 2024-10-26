export default class Currency {
  constructor(code, name) {
    this._code = this._validateCode(code);
    this._name = this._validateName(name);
  }

  // Getter and setter for code
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this._validatCode(value);
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateName(value);
  }

  // Method to display full currency
  // eslint-disable-next-line class-methods-use-this
  displayFullCurrency() {
    // eslint-disable-next-line no-template-curly-in-string
    return '${this._name} (${this._code})';
  }

  // Validation methods
  // eslint-disable-next-line class-methods-use-this
  _validateCode(code) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    return code;
  }

  // eslint-disable-next-line class-methods-use-this
  _validateName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    return name;
  }
}
