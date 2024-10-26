const brandSymbol = Symbol('brand');
const motorSymbol = Symbol('motor');
const colorSymbol = Symbol('color');

export default class Car {
  constructor(brand, motor, color) {
    this[brandSymbol] = brand;
    this[motorSymbol] = motor;
    this[colorSymbol] = color;
  }

  // Getter for brand
  get brand() {
    return this[brandSymbol];
  }

  // Getter for motor
  get motor() {
    return this[motorSymbol];
  }

  // Getter for color
  get color() {
    return this[colorSymbol];
  }

  // Method to clone the car
  cloneCar() {
    return new Car(this.brand, this.motor, this.color);
  }
}

// Example usage
const car1 = new Car('Toyota', 'V6', 'Red');
const car2 = car1.cloneCar();

console.log(car1); // Original car
console.log(car2); // Cloned car
console.log(car1 === car2); // Should be false (different instances)