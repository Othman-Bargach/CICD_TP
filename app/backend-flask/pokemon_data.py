import random, requests
from random_id import random_id

pokeapi_uri = "https://pokeapi.co/api/v2/pokemon/" # URI base for API calls
# The types_colours variable could be moved to a json file because this is just awful
types_colours = {"bug":"#94BC4A",
                 "dark":"#736C75",
                 "dragon":"#6A7BAF",
                 "electric":"#E5C531",
                 "fairy":"#E39741",
                 "fighting":"#CB5F48",
                 "fire":"#EA7A3C",
                 "flying":"#7DA6DE",
                 "ghost":"#846AB6",
                 "grass":"#71C558",
                 "ground":"#CC9F4F",
                 "ice":"#70CBD4",
                 "normal":"#AAB09F",
                 "poison":"#B468B7",
                 "psychic":"#E5709B",
                 "rock":"#B2A061",
                 "steel":"#89A1B0",
                 "water":"#539AE2",
                 "nosecondtype":"#49454F"}

class pokemon_data():
    def __init__(self, pokemon_name, artwork, pokedex_id, pokedex_link, type1, type1_colour, type2, type2_colour):
        self.pokemon_name = pokemon_name
        self.artwork = artwork
        self.pokedex_id = pokedex_id
        self.type1 = type1
        self.type1_colour = type1_colour
        self.type2 = type2
        self.type2_colour = type2_colour
        self.pokedex_link = pokedex_link

def get_pokemon():
    pokemon_id = random_id() # Leverage the random_id() function to get a random pokémon ID from the list
    random_pokemon = requests.get(url = pokeapi_uri + str(pokemon_id) + "/").json() # HTTP request to get the pokémon's data
    random_pokemon_species = requests.get(url = random_pokemon['species']['url']).json() # Second HTTP request to get additional data
    artwork = random_pokemon['sprites']['other']['official-artwork']['front_default']
    pokemon_name = random_pokemon_species['name']
    pokedex_id = random_pokemon_species['id']
    pokedex_link = "https://pokemondb.net/pokedex/" + pokemon_name # Complete pokédex entry
    type1 = random_pokemon['types'][0]['type']['name']
    type1_colour = types_colours[type1]
    try:
        type2 = random_pokemon['types'][1]['type']['name']
    except:
        type2 = 'nosecondtype'
    type2_colour = types_colours[type2]
    return pokemon_data(pokemon_name, artwork, pokedex_id, pokedex_link, type1, type1_colour, type2, type2_colour)