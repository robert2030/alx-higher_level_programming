#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const secondLargest = args[1];
  console.log(secondLargest);
}
