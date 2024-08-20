#!/usr/bin/node

const request = require('request');

const movieid = process.argv[2];
const apiurl = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request.get(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  }
});
