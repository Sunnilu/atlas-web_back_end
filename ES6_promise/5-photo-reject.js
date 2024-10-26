/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable import/no-self-import */
import uploadPhoto from './5-photo-reject';

describe('uploadPhoto', () => {
  it('should reject with an error message', async () => {
    await expect(uploadPhoto('guillaume.jpg')).rejects.toThrow('guillaume.jpg cannot be processed');
  });
});
