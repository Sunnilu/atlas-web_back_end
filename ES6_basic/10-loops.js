export default function appendToEachArrayValue(array, appendString) {
  const newArray = []; // Create a new array to hold modified values
  for (const value of array) {
    newArray.push(appendString + value); // Append the string and push to new array
  }
  return newArray; // Return the new array instead of modifying the original
}
