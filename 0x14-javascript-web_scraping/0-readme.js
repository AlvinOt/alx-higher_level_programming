#!/usr/bin/node

const filesys = require('fs');
const filename = process.argv[2];

filesys.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
