#!/usr/bin/node
/*
* Script to display status code of a GET request.
* The first argument is URL to request
* The status code must be printed like this: code: <status code>
*/
const url = process.argv[2];
const request = require('request');
request(url, function (err, result, body) {
  console.log('code: ' + result.statusCode);
  if (err) {
    console.log(err);
  }
});
