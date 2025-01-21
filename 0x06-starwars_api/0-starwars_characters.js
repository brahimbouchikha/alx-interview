#!/usr/bin/node

const request = require('request');

const printCharacterNames = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printCharacterNames(characters, index + 1);
  });
};

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  printCharacterNames(characters, 0);
});
