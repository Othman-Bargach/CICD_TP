const IP = '54.77.254.30';

// Script to manage Pokémon card UI and fetch data from the API

// Update the UI with Pokémon data
function updatePokemonCard(pokemon) {
    const type1El = document.getElementById('type1');
    const type2El = document.getElementById('type2');

    document.getElementById('pokemon_name').textContent = pokemon.pokemon_name;
    document.getElementById('pokedex_number').textContent = `#${pokemon.pokedex_id}`;

    type1El.textContent = pokemon.type1;
    type1El.style.backgroundColor = pokemon.type1_colour;

    if (pokemon.type2 !== 'nosecondtype') {
        type2El.textContent = pokemon.type2;
        type2El.style.backgroundColor = pokemon.type2_colour;
        type2El.style.display = 'inline';
        type2El.style.marginLeft = '5px';
        type1El.style.marginRight = '5px';
    } else {
        type2El.style.display = 'none';
        type2El.style.marginLeft = '0px';
        type1El.style.marginRight = '0px';
    }

    document.getElementById('art').src = pokemon.artwork;
    document.getElementById('pokedex_entry').href = pokemon.pokedex_link;
}

// Fetch and store Pokémon data, then update the UI
function fetchAndDisplayPokemon() {
    fetch(`http://${IP}:5000/call_results`)
        .then(response => response.json())
        .then(pokemon => {
            localStorage.setItem('pokemonData', JSON.stringify(pokemon));
            updatePokemonCard(pokemon);
        })
        .catch(error => {
            console.error('Error fetching Pokémon data:', error);
        });
}

// On first button click
document.getElementById('initial_button').addEventListener('click', () => {
    fetchAndDisplayPokemon();
    document.getElementById('initial_button').style.display = 'none';
    document.getElementById('container').style.display = 'block';
});

// On page load
window.addEventListener('load', () => {
    const savedData = localStorage.getItem('pokemonData');

    if (savedData) {
        const pokemon = JSON.parse(savedData);
        updatePokemonCard(pokemon);
        document.getElementById('initial_button').style.display = 'none';
        document.getElementById('container').style.display = 'block';
    } else {
        document.getElementById('initial_button').style.display = 'block';
        document.getElementById('container').style.display = 'none';
    }
});

// On randomize button click
document.getElementById('randomize').addEventListener('click', () => {
    fetchAndDisplayPokemon();
});
