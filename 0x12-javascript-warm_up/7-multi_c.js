#!/usr/bin/node
const multi_c = process.argv[2];

if (!parseInt(multi_c)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < multi_c; i++) {
    console.log('C is fun');
  }
}
