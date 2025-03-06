// 5-subscriber.js
const redis = require('redis');
const subscriber = redis.createClient();

subscriber.on('connect', function() {
    console.log('Redis client connected to the server');
});

subscriber.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.subscribe('holberton school channel', function(err, count) {
    if (err) {
        console.log(`Error subscribing to channel: ${err.message}`);
        return;
    }
});

subscriber.on('message', function(channel, message) {
    console.log(`Received message on channel "${channel}": ${message}`);
    
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
