import requests, re, random

def random_id():
    pokeapi_uri = "https://pokeapi.co/api/v2/pokemon/?limit=9999" # Not exactly a fancy way, but it took GameFreaks 28 years to release 1025 pokémon so this code should be ok for 270 years

    resource_list = requests.get(url = pokeapi_uri).json() # Pass the API content in a variable
    pokelist = resource_list['results'] # Retrieve the results in a dictionary
    idlist = [] # Initiate an empty list
    for i in pokelist:
        idlist.append(re.findall(r'[^\d]*[\d]+[^\d]+([\d]+)',i['url'])[0]) # Loop through the results, retrieve the pokémon ID from the URL using regex and append it to the list

    random_id = random.choice(idlist) # Get a random pokémon ID from the list

    return random_id