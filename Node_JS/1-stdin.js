const readline = require('readline');

// Create an interface to read from standard input (stdin) and write to standard output (stdout)
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Display the welcome message
rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  // Output the user's name
  console.log(`Your name is: ${name}`);
  
  // After displaying the name, close the program with the final message
  rl.close();
});

// Display the closing message when the program ends
rl.on('close', () => {
  console.log('This important software is now closing');
});
