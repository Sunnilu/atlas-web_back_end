/* eslint-disable import/extensions */
import { uploadPhoto, createUser } from './utils.js';

// eslint-disable-next-line no-unused-vars
function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    // eslint-disable-next-line no-unused-vars
    .then(([photoResponse, userResponse]) => {
      console.log(`First Name: ${userResponse.body.firstName}`);
      console.log(`Last Name: ${userResponse.body.lastName}`);
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
