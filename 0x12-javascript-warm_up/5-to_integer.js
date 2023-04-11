#!/usr/bin/node

const parsedNum = parseInt(process.argv[2]);
console.log(parsedNum ? 'My number: ' + process.argv[2] : 'Not a number');
