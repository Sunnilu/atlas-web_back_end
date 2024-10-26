// 2-then.js
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
