const kue = require('kue');
const queue = kue.createQueue();

// Function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the queue
queue.process('push_notification_code', function(job, done) {
  try {
    // Extract phone number and message from job data
    const { phoneNumber, message } = job.data;
    
    // Send the notification
    sendNotification(phoneNumber, message);
    
    // Complete the job
    done();
  } catch (error) {
    // If there's an error, mark the job as failed
    done(error);
  }
});

// Handle any queue errors
queue.on('error', (err) => {
  console.error('Queue error:', err);
});