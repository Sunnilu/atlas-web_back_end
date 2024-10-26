// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an asynchronous operation (like an API call)
    setTimeout(() => {
      // it can resolve with a value or reject with an error
      resolve("Response from API");
    }, 1000; // Simulate a delay of 1 second
  });
}