const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
  // Validate that jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Create a queue if none was provided
  if (!queue) {
    queue = kue.createQueue();
  }

  // Process each job in the array
  jobs.forEach((jobData) => {
    // Create a new job in the queue
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (err) {
          console.error('Error creating job:', err);
          return;
        }
        console.log(`Notification job created: ${job.id}`);
      });

    // Handle job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Handle job failure
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Handle job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });

  // Return the queue for chaining
  return queue;
}

// Export the function
module.exports = createPushNotificationsJobs;