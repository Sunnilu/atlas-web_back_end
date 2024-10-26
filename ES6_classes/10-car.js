const brandSymbol = Symbol('brand');
const motorSymbol = Symbol('motor');
const colorSymbol = Symbol('color');

export default class Car {
  constructor(brand, motor, color) {
    this[brandSymbol] = brand;
    this[motorSymbol] = motor;
    this[colorSymbol] = color;
  }

  // Method to clone the car
  cloneCar() {
    return new Car(this[brandSymbol], this[motorSymbol], this[colorSymbol]);
  }

  // Getter to access private attributes
  get _brand() {
    return this[brandSymbol];
  }

  get _motor() {
    return this[motorSymbol];
  }

  get _color() {
    return this[colorSymbol];
  }
}

// Example usage for testing
const testCar = new Car('Nissan', 'Turbo', 'Pink');
console.log(testCar); // Should show the car details

// Verify clone functionality
const clonedCar = testCar.cloneCar();
console.log(clonedCar); // Should show cloned car details

// Checking instance types
console.log(testCar instanceof Car); // true
console.log(clonedCar instanceof Car); // true

// Verifying equality of instances
console.log(testCar === clonedCar); // false (different instances)
