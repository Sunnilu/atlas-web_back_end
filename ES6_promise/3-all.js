/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
// 3-all.js

import { uploadPhoto, createUser } from './utils.js';

export function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    // eslint-disable-next-line no-unused-vars
    .then(([photoResponse, userResponse]) => {
      console.log(`First Name: ${userResponse.body.firstName}`);
      console.log(`Last Name: ${userResponse.body.lastName}`);
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
