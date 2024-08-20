#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, function (err, response, body) {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
