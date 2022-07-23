import os
import requests


def get_droplets():
    url = 'https://api.digitalocean.com/v2/droplets'
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    droplets = r.json()
    droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i])
    return droplet_list


def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0'
    response = requests.get(url)
    pokemon = response.json()
    pokemon_list = []
    for i in range(len(pokemon['results'])):
        pokemon_list.append(pokemon['results'][i])
    return pokemon_list


def get_categorys():
    url = 'https://blog-django-rest.herokuapp.com/api/categories/'
    r = requests.get(url)
    categorys = r.json()
    categorys_list = []
    for i in range(len(categorys)):
        categorys_list.append(categorys[i])
    return categorys_list

