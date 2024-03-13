#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    let i, j;
    let xString = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        xString += c;
      }
      console.log(xString);
      xString = '';
    }
  }
}

module.exports = Square;
