// 8-clean_set.js
export default function cleanSet(set, startString) {
  // Check if startString is empty and return an empty string if so
  if (tyoeof startString !== 'string' || startString === '') {
    return '';
  }

  // Filter the set and join the results
  return [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-'); // Join them with '-'
}
