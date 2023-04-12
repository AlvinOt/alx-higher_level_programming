#!/usr/bin/node

const sqSz = Number(process.argv[2]);
if (isNaN(sqSz)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqSz; i++) {
    console.log(('X').repeat(sqSz));
  }
}
