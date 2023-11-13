#!/usr/bin/node

/* a script that computes and prints a factorial */

const process = require('process');

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const num = Number.parseInt(process.argv[2]);

if (!num) {
  console.log(1);
} else {
  console.log(factorial(num));
}
