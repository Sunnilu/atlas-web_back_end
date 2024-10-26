// eslint-disable-next-line import/extensions
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = this._validateAmount(amount);
    this._currency = this._validateCurrency(currency);
  }

  // Amount getter
  get amount() {
    return this._amount;
  }

  // Amount setter
  set amount(value) {
    this._amount = this._validateAmount(value);
  }

  // Currency getter
  get currency() {
    return this._currency;
  }

  // Currency setter
  set currency(value) {
    this._currency = this._validateCurrency(value);
  }

  // Method to display full price
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method to convert price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  // Validation methods
  // eslint-disable-next-line class-methods-use-this
  _validateAmount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    return amount;
  }

  // eslint-disable-next-line class-methods-use-this
  _validateCurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency');
    }
    return currency;
  }
}
