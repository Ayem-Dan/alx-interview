#!/usr/bin/node
const https = require('https');

// Define the Star Wars API base URL
const BASE_URL = "https://swapi.dev/api";

// Parse the Movie ID from the command-line arguments
if (process.argv.length < 3) {
    console.error("Usage: node script.js <Movie ID>");
    process.exit(1);
}

const movie_id = parseInt(process.argv[2]);

// Fetch the movie data from the Star Wars API
https.get(`${BASE_URL}/films/${movie_id}`, (res) => {
    let data = "";

    res.on('data', (chunk) => {
        data += chunk;
    });

    res.on('end', () => {
        if (res.statusCode !== 200) {
            console.error("Error: Could not fetch movie data");
            process.exit(1);
        }

        const movie_data = JSON.parse(data);

        // Fetch the character data for the movie
        const characters = movie_data.characters;

        characters.forEach((character_url) => {
            https.get(character_url, (res) => {
                let data = "";

                res.on('data', (chunk) => {
                    data += chunk;
                });

                res.on('end', () => {
                    if (res.statusCode !== 200) {
                        console.error("Error: Could not fetch character data");
                        process.exit(1);
                    }

                    const character_data = JSON.parse(data);
                    console.log(character_data.name);
                });
            }).on('error', (err) => {
                console.error(err);
            });
        });
    });
}).on('error', (err) => {
    console.error(err);
});
