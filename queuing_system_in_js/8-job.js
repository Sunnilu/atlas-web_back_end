import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
  // Validate input
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Handle empty array case
  if (jobs.length === 0) {
    return;
  }

  // Create jobs for each item in the array
  jobs.forEach(job => {
    const kueJob = queue.create('push_notification_code_3', job)
      .removeOnComplete(true);

    // Log job creation
    console.log(`Notification job created: ${kueJob.id}`);

    // Handle job completion
    kueJob.on('complete', () => {
      console.log(`Notification job ${kueJob.id} completed`);
    });

    // Handle job failure
    kueJob.on('failed', (errorMessage) => {
      console.log(`Notification job ${kueJob.id} failed: ${errorMessage}`);
    });

    // Handle job progress
    kueJob.on('progress', (progress) => {
      console.log(`Notification job ${kueJob.id} ${progress}% complete`);
    });

    // Force save to ensure job is persisted
    kueJob.save(err => {
      if (err) {
        console.error(`Error saving job ${kueJob.id}: ${err.message}`);
      }
    });
  });
}