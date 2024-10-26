// 7-has_array_value.js
export default function hasValuesFromArray(set, array) {
  // Use the every method to check if all elements in the array are in the set
  return array.every((element) => set.has(element));
}
