import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((responses) => {
      // eslint-disable-next-line no-unused-vars
      const [photoResponse, userResponse] = responses;
      console.log(`${userResponse.body.firstName} ${userResponse.body.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
