// eslint-disable-next-line no-unused-vars
class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Convert the class instance to a Number
  valueOf() {
    return this._size;
  }

  // Convert the class instance to a String
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
