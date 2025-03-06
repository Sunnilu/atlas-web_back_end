const assert = require('assert');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Enter test mode before running tests
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    // Exit test mode and clear the queue after tests
    queue.testMode.exit();
    queue.testMode.clear();
  });

  it('should throw an error when jobs is not an array', () => {
    assert.throws(() => createPushNotificationsJobs('not an array', queue), 
      Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate jobs in queue
    assert.strictEqual(queue.testMode.jobs.length, 2);
    assert.strictEqual(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert.strictEqual(queue.testMode.jobs[1].type, 'push_notification_code_3');
  });

  it('should handle empty array', () => {
    const jobs = [];
    createPushNotificationsJobs(jobs, queue);
    assert.strictEqual(queue.testMode.jobs.length, 0);
  });

  it('should create jobs with correct data', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' }
    ];

    createPushNotificationsJobs(jobs, queue);
    const job = queue.testMode.jobs[0];
    assert.deepStrictEqual(job.data, jobs[0]);
  });

  it('should handle multiple jobs with different data', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' },
      { phoneNumber: '4153518782', message: 'Test message 3' }
    ];

    createPushNotificationsJobs(jobs, queue);

    assert.strictEqual(queue.testMode.jobs.length, 3);
    jobs.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];
      assert.deepStrictEqual(job.data, jobData);
      assert.strictEqual(job.type, 'push_notification_code_3');
    });
  });

  it('should handle jobs with missing required fields', () => {
    const jobs = [
      { message: 'Test message 1' }, // Missing phoneNumber
      { phoneNumber: '4153518780' }  // Missing message
    ];

    assert.throws(() => createPushNotificationsJobs(jobs, queue),
      Error, 'Missing required fields');
  });
});