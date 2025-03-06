const kue = require('kue');
const createPushNotificationsJobs = require('./8-job'); // Adjust the path if necessary
const assert = require('assert');
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode = true; // Enable test mode
  });

  afterEach(() => {
    queue.testMode = false; // Exit test mode after each test
    queue.removeCompleted(); // Clear the queue after tests
  });

  it('should display an error message if jobs is not an array', () => {
    const invalidJobs = 'not an array';
    const result = createPushNotificationsJobs(invalidJobs, queue);
    assert.strictEqual(result, 'Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Notification 1' },
      { phoneNumber: '456', message: 'Notification 2' }
    ];

    const result = createPushNotificationsJobs(jobs, queue);

    // Validate the jobs in the queue
    queue.process((job, done) => {
      console.log(`Notification job created: ${job.data.phoneNumber}`);
      done();
    });

    // Check that two jobs were added to the queue
    assert.strictEqual(queue.testMode.jobs.length, 2);  // Expect 2 jobs in the queue
    assert.strictEqual(queue.testMode.jobs[0].data.phoneNumber, '123');
    assert.strictEqual(queue.testMode.jobs[1].data.phoneNumber, '456');
  });

  it('should not add jobs to the queue if an empty array is passed', () => {
    const emptyJobs = [];
    const result = createPushNotificationsJobs(emptyJobs, queue);

    // Ensure no jobs were added
    assert.strictEqual(queue.testMode.jobs.length, 0);
  });

  // Add more test cases as needed...
});
