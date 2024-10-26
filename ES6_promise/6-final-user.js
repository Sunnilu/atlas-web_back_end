// eslint-disable-next-line import/extensions
import signUpUser from './4-user-promise.js';
// eslint-disable-next-line import/extensions
import uploadPhoto from './5-photo-reject.js';

// eslint-disable-next-line import/prefer-default-export
export async function handleProfileSignup(firstName, lastName, fileName) {
  const results = await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);

  return results.map((result) => ({
    status: result.status,
    value: result.status === 'fulfilled' ? result.value : result.reason,
  }));
}
