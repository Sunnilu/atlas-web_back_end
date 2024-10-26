import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((responses) => {
      // eslint-disable-next-line no-undef, no-unused-vars
      const [photoResponse, userResponse] = responses;
      // eslint-disable-next-line no-template-curly-in-string
      console.log('${userResponse.body.firstName} ${userResponse.body.lastName}');
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
