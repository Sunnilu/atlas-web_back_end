/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
// 6-final-user.js
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

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
// eslint-disable-next-line no-multiple-empty-lines

