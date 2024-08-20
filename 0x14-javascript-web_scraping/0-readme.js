#!/usr/bin/node

const fs = require('fs');
try {
  fs.readFile(process.argv[2], 'utf8', function (err, data) {
    if (err) {
      console.error(err);
      return;
    }
    process.stdout.write(data);
  });
} catch (err) {
  console.error(err);
}
