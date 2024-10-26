// eslint-disable-next-line import/extensions
import { uploadPhoto, createUser } from './utils.js';

// eslint-disable-next-line no-unused-vars
function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    // eslint-disable-next-line no-unused-vars
    .then(([photoResponse, userResponse]) => {
      console.log(`First Name: ${userResponse.firstName}`);
      console.log(`Last Name: ${userResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
