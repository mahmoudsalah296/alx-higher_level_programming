#!/usr/bin/node

/**
 * a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */

const process = require('process');
const arg = Number.parseInt(process.argv[2]);
if (arg) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
