// 8-clean_set.js
export default function cleanSet(set, startString) {
  // Check if startString is empty and return an empty string if so
  if (startString === '') {
    return '';
  }

  // Use the filter method to find matching values, then map to get the rest of the string
  const result = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('');

  return result;
}
