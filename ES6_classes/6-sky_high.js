// eslint-disable-next-line import/extensions
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call the parent class constructor
    this._floors = this._validateFloors(floors);
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Override the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }

  // Validation method for floors
  // eslint-disable-next-line class-methods-use-this
  _validateFloors(floors) {
    if (typeof floors !== 'number') {
      throw new TypeError('floors must be a number');
    }
    return floors;
  }
}
