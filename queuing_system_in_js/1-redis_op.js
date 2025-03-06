const redis = require('redis');
const client = redis.createClient();

client.on('connect', function() {
    console.log('Connected to Redis!');
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, function(err, reply) {
        if (err) {
            console.log(`Error getting ${schoolName}: ${err}`);
            return;
        }
        console.log(reply);
    });
}

// Call the functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');