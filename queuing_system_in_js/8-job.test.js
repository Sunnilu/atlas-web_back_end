import kue from 'kue';
import createPushNotificationsJobs from './push-notifications';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue({
    prefix: 'tests',
    redis: {
      port: 6379,
      host: 'localhost'
    }
  });

  beforeAll(async () => {
    // Enter test mode to prevent job processing
    queue.testMode.enter();
  });

  afterEach(async () => {
    // Clear the queue after each test
    await queue.testMode.clear();
  });

  afterAll(async () => {
    // Exit test mode after all tests
    queue.testMode.exit();
  });

  describe('Input Validation', () => {
    it('should display error message if jobs is not an array', async () => {
      await expect(createPushNotificationsJobs(queue, 'invalid')).rejects.toThrow(
        'jobs must be an array'
      );
    });
  });

  describe('Job Creation', () => {
    it('should create two new jobs to the queue', async () => {
      const jobs = [
        { id: 1, data: { message: 'Notification 1' } },
        { id: 2, data: { message: 'Notification 2' } }
      ];

      await createPushNotificationsJobs(queue, jobs);

      const jobCount = await queue.testMode.find('notification');
      expect(jobCount.length).toBe(2);

      // Verify job details
      const [job1] = await queue.testMode.find({ id: 1 });
      expect(job1.data.message).toBe('Notification 1');
    });
  });

  describe('Error Handling', () => {
    it('should handle empty array gracefully', async () => {
      await expect(createPushNotificationsJobs(queue, [])).resolves.not.toThrow();
      
      const jobCount = await queue.testMode.find('notification');
      expect(jobCount.length).toBe(0);
    });
  });
});