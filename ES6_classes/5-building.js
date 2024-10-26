export default class Building {
  constructor(sqft) {
    this._sqft = this._validateSqft(sqft);

    // Check if the subclass has overridden the method
    if (new.target !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Method to be implemented by subclasses
  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }

  // Validation method
  // eslint-disable-next-line class-methods-use-this
  _validateSqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    return sqft;
  }
}
