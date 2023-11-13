#!/usr/bin/node

/**
 * a script that prints x times “C is fun”
 */
const process = require('process');
const arg = Number.parseInt(process.argv[2]);

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
