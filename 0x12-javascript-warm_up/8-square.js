#!/usr/bin/node
const size = process.argv[2];

const num = Number(size);

if (!isNaN(num)) {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      let line = '';
      for (let j = 0; j < num; j++) {
        line += 'X';
      }
      console.log(line);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
