import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(() => {
      // eslint-disable-next-line no-undef
      const [] = responses;
      // eslint-disable-next-line no-template-curly-in-string
      console.log('${userResponse.body.firstName} ${userResponse.body.lastName}');
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
