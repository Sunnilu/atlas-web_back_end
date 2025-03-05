const redis = require('redis');
const util = require('util');

const client = redis.createClient();

client.on('connect', function() {
    console.log('Connected to Redis!');
});

// Promisify redis.get
client.getAsync = util.promisify(client.get);

async function displaySchoolValue(schoolName) {
    try {
        const value = await client.getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.log(`Error getting ${schoolName}: ${err}`);
    }
}

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Call the functions as specified
async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

main();

