// 5-typed_arrays.js
// eslint-disable-next-line no-unused-vars
export default function createInt8TypedArray(length, position, value) {
  // check if the position is within the valid range
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer and an Int8Array view
  const buffer = new ArrayBuffer(length);
  const int8Array = new Int8Array(buffer);
  int8Array[position] = value;

  return int8Array;
}
