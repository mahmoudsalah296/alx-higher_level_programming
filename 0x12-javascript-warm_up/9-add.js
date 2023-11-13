#!/usr/bin/node

/* a script that prints the addition of 2 integers */

const process = require('process');

function add(a, b) {
  return a + b;
}

const first = Number.parseInt(process.argv[2]);
const second = Number.parseInt(process.argv[3]);

console.log(add(first, second));
