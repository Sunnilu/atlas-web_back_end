const kue = require('kue');
const createPushNotificationsJobs = require('./8-job'); // Adjust the path if necessary
const assert = require('assert');
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode = true; // Enable test mode to prevent job processing
  });

  afterEach(() => {
    queue.testMode = false; // Exit test mode after each test
    queue.removeJobs(['push_notification_code_3']); // Clear the specific job type from the queue
  });

  it('should display an error message if jobs is not an array', () => {
    const invalidJobs = 'not an array'; // Passing a string instead of an array
    const result = createPushNotificationsJobs(invalidJobs, queue); // Call the function
    assert.strictEqual(result, 'Jobs is not an array'); // Assert the error message
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Notification 1' },
      { phoneNumber: '456', message: 'Notification 2' }
    ];

    const result = createPushNotificationsJobs(jobs, queue); // Call the function to add jobs

    // Validate the jobs in the queue
    queue.process('push_notification_code_3', (job, done) => {
      console.log(`Notification job created: ${job.data.phoneNumber}`);
      done();
    });

    // Ensure two jobs are in the queue
    assert.strictEqual(queue.testMode.jobs.length, 2); // Check the number of jobs in the queue
    assert.strictEqual(queue.testMode.jobs[0].data.phoneNumber, '123'); // First job's phone number
    assert.strictEqual(queue.testMode.jobs[1].data.phoneNumber, '456'); // Second job's phone number
  });

  it('should not add jobs to the queue if an empty array is passed', () => {
    const emptyJobs = []; // Passing an empty array
    const result = createPushNotificationsJobs(emptyJobs, queue); // Call the function with empty array

    // Ensure no jobs were added to the queue
    assert.strictEqual(queue.testMode.jobs.length, 0); // No jobs should be in the queue
  });

  it('should not add jobs to the queue if jobs is not an array', () => {
    const invalidJobs = 'not an array'; // Invalid input
    const result = createPushNotificationsJobs(invalidJobs, queue); // Call the function with invalid input

    // Ensure no jobs were added to the queue
    assert.strictEqual(queue.testMode.jobs.length, 0); // No jobs should be added
  });
});
