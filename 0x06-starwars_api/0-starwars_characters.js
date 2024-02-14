#!/usr/bin/node

const request = require('request');

function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
        } else if (response.statusCode !== 200) {
            console.error('Unexpected status code:', response.statusCode);
        } else {
            const film = JSON.parse(body);
            film.characters.forEach(characterUrl => {
                request(characterUrl, (error, response, body) => {
                    if (!error && response.statusCode === 200) {
                        const character = JSON.parse(body);
                        console.log(character.name);
                    } else {
                        console.error('Error fetching character:', error);
                    }
                });
            });
        }
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

getCharacters(movieId);

