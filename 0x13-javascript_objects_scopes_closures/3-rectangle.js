#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log('Empty object');
    } else {
      for (let count = 0; count < this.height; count++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
