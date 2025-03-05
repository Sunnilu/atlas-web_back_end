const kue = require('kue');
const queue = kue.createQueue();

// Create job data
const jobData = {
    phoneNumber: '+1234567890',
    message: 'Hello from Kue!'
};

// Create and save the job
queue.create('push_notification_code', jobData)
    .on('complete', () => {
        console.log('Notification job completed');
    })
    .on('failed', () => {
        console.log('Notification job failed');
    })
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${queue.id}`);
        }
    });