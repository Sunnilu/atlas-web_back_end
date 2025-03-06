const redis = require('redis');
const client = redis.createClient();

client.on('connect', function() {
    console.log('Connected to Redis!');
    
    // Store hash values
    client.hset('HolbertonSchools', 'Portland', '50', redis.print);
    client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
    client.hset('HolbertonSchools', 'New York', '20', redis.print);
    client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
    client.hset('HolbertonSchools', 'Cali', '40', redis.print);
    client.hset('HolbertonSchools', 'Paris', '2', redis.print);

    // Display all hash values
    client.hgetall('HolbertonSchools', function(err, reply) {
        if (err) {
            console.log('Error:', err);
            return;
        }
        console.log('\nStored hash values:');
        console.log(reply);
    });
}); 