#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  if (list.length === 0) return 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { counter++; }
  }
  return counter;
};
