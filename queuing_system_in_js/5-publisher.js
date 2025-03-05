// 5-publisher.js
const redis = require('redis');
const publisher = redis.createClient();

publisher.on('connect', function() {
    console.log('Redis client connected to the server');
});

publisher.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school channel', message);
    }, time);
}

// Example usage:
publishMessage("Hello!", 1000);