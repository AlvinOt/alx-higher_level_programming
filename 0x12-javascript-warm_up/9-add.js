#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];

function add (num1, num2) {
  return (num1 + num2);
}

console.log(add(parseInt(num1), parseInt(num2)));
