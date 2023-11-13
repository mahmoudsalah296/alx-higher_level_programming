#!/usr/bin/node

/* a script that searches the second biggest integer in the list of arguments */

const process = require('process');
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  let biggest = process.argv[2];
  let secondBiggest = process.argv[3];

  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      const tmp = biggest;
      biggest = process.argv[i];
      secondBiggest = tmp;
    }
  }
  console.log(secondBiggest);
}
