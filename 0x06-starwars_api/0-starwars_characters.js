#!/usr/bin/node
// Script to print all characters of a Star Wars movie using the Star Wars API

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error fetching the movie details:', err);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error('Failed to fetch movie details. Status code:', res.statusCode);
    process.exit(1);
  }

  const characters = body.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error('Error fetching character details:', err);
        return;
      }

      if (res.statusCode !== 200) {
        console.error('Failed to fetch character details. Status code:', res.statusCode);
        return;
      }

      console.log(body.name);
    });
  });
});
