#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  const reversedList = [];

  while (i >= 0) {
    reversedList.push(list[i]);
    i--;
  }
  return reversedList;
};
