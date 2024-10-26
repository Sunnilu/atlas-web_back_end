// Example function that returns a value
const exampleFunction = () => 1000;

// Example function that throws an error
const errorFunction = () => {
  throw new Error('Something went wrong!');
};

// Using guardrail
// eslint-disable-next-line no-undef
console.log(guardrail(exampleFunction)); // Output: [1000, 'Guardrail was processed']
// eslint-disable-next-line max-len, no-undef
console.log(guardrail(errorFunction)); // Output: ['Something went wrong!', 'Guardrail was processed']
