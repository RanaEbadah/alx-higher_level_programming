#!/usr/bin/node
function factorialCalc (n) {
    if (n === 0 || isNaN(n)) {
      return (1);
    }
    if (n < 0) {
      return (-1);
    }
    return (n * factorialCalc(n - 1));
  }
  
  console.log(factorialCalc(Number(process.argv[2])));
  