#!/usr/bin/node

/* script that prints a square usin 'X' */

const process = require('process');
const size = Number.parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
