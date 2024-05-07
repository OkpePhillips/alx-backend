const kue = require('kue');
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track the progress of the job

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed(new Error(errorMessage));
    console.error(errorMessage);
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100); // Update progress to 50%
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done(); // Notify Kue that the job processing is complete
  }
}

// Process jobs from the 'push_notification_code_2' queue with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
