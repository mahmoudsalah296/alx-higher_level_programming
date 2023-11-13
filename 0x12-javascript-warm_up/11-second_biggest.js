#!/usr/bin/node

/* a script that searches the second biggest integer in the list of arguments */

const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args.sort(function (a, b) {
    return b - a;
  });
  console.log(args[1]);
}
