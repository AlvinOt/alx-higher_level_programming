#!/usr/bin/node
const multiC = process.argv[2];

if (!parseInt(multiC)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < multiC; i++) {
    console.log('C is fun');
  }
}
