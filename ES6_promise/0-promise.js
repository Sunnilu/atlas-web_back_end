// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Simulate an asynchronous operation (like an API call)
    setTimeout(() => {
      resolve('Response from API');
    }, 1000); // Simulate a delay of 1 second
  });
}
