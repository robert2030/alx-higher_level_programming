#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      console.log(films.reduce((count, movie) => {
        return movie.characters.find((character) => character.includes('/18/'))
          ? count + 1
          : count;
      }, 0));
    }
  }
});
