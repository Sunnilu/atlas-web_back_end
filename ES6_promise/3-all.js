/* eslint-disable import/prefer-default-export */
// 3-all.js

import { uploadPhoto, createUser } from './utils';

export function handleProfileSignup() {
  const firstName = 'Bob';
  const lastName = 'Dylan';

  Promise.all([uploadPhoto(), createUser(firstName, lastName)])
    // eslint-disable-next-line no-unused-vars
    .then(([photoData, userData]) => {
      console.log(`firstName: ${userData.firstName}`);
      console.log(`lastName: ${userData.lastName}`);
    })
    // eslint-disable-next-line no-unused-vars
    .catch((error) => {
      // eslint-disable-next-line quotes
      console.error("Signup system offline");
    });
}
