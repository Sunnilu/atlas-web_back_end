const kue = require('kue');
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

// Function to send notifications with progress tracking
function sendNotification(phoneNumber, message, job, done) {
  // Track initial progress
  job.progress(0, 100);
  
  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
    return;
  }
  
  // Track progress to 50%
  job.progress(50, 100);
  
  // Log the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
  // Complete the job
  done();
}

// Process jobs from the queue with concurrency of 2
queue.process('push_notification_code_2', 2, function(job, done) {
  try {
    // Extract phone number and message from job data
    const { phoneNumber, message } = job.data;
    
    // Send the notification
    sendNotification(phoneNumber, message, job, done);
  } catch (error) {
    // If there's an error, mark the job as failed
    done(error);
  }
});

// Handle any queue errors
queue.on('error', (err) => {
  console.error('Queue error:', err);
});