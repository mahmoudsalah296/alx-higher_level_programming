#!/usr/bin/node

/* a script that prints a message depending of the number of arguments passed */
const process = require('process');

if (process.argv.length <= 2) {
  console.log('No arguments');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
