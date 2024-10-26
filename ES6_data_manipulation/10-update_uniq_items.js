// 10-update_uniq_items.js
export default function updateUniqueItems(groceries) {
  // check if the argument is a Map
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate through the entries of the map
  for (const [key, value] of groceries.entries()) {
    // If the quantity is 1, update it to 100
    if (value === 1) {
      groceries.set(key, 100);
    }
  }
}
