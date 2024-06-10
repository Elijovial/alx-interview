#!/usr/bin/node

const axios = require('axios');

async function starwarsCharacters(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  try {
    const response = await axios.get(endpoint);
    const characters = response.data.characters;

    for (let i = 0; i < characters.length; i++) {
      const characterUrl = characters[i];
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

const filmId = process.argv[2];
starwarsCharacters(filmId);
