// 6-final-user.test.js
import { handleProfileSignup } from './6-final-user.js'; // Use curly braces for named import

test("handleProfileSignup returns the right array", async () => {
  const queue = await handleProfileSignup('John', 'Doe', 'Gerald.jpg');
  expect(queue).toEqual([
    {
      status: 'fulfilled',
      value: expect.anything(), // adjust according to what signUpUser returns
    },
    {
      status: 'fulfilled',
      value: expect.anything(), // adjust according to what uploadPhoto returns
    },
  ]);
});

