#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let xString = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        xString += 'X';
      }
      console.log(xString);
      xString = '';
    }
  }
}

module.exports = Rectangle;
