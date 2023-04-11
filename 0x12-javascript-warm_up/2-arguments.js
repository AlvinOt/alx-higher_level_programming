#!/usr/bin/node

const countr = process.argv.length;
console.log(countr === 2 ? 'No argument' : countr === 3 ? 'Argument found' : 'Arguments found');
