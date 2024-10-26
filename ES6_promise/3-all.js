/* eslint-disable import/extensions */
// 3-correct-text.test.js
// eslint-disable-next-line import/no-unresolved
import handleProfileSignup from './3-correct-text';
import { uploadPhoto, createUser } from './utils';

jest.mock('./utils');

describe('handleProfileSignup', () => {
  // eslint-disable-next-line jest/prefer-expect-assertions
  it('returns the right text', async () => {
    const spy = jest.spyOn(console, 'log').mockImplementation();

    // Mock implementations
    uploadPhoto.mockResolvedValue({ url: 'photo-profile-1' });
    createUser.mockResolvedValue({
      body: {
        firstName: 'Guillaume',
        lastName: 'Salva',
      },
    });

    await handleProfileSignup();

    // eslint-disable-next-line jest/no-alias-methods
    expect(spy).toBeCalledWith('photo-profile-1 Guillaume Salva');
    spy.mockRestore();
  });
});
