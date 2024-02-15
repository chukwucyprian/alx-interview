#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
  // Check if filmID is provided
  if (!filmId) {
    console.error('Please provide a valid movie ID as the first argument.');
    process.exit(1);
  }

  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;

  try {
    let response = await request(endpoint);
    if (response.statusCode !== 200) {
      console.error('Failed to fetch movie details. Status Code:', response.statusCode);
      process.exit(1);
    }
    
    let characters = JSON.parse(response.body).characters;

    if (!characters || characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      try {
        let characterResponse = await request(urlCharacter);
        if (characterResponse.statusCode !== 200) {
          console.error('Failed to fetch character details. Status Code:', characterResponse.statusCode);
          continue;
        }
        let character = JSON.parse(characterResponse.body);
        console.log(character.name.trim()); // Trim whitespace from character name
      } catch (error) {
        console.error('Error fetching character:', error.message);
      }
    }
  } catch (error) {
    console.error('Error fetching movie details:', error.message);
  }
}

starwarsCharacters(filmID);
