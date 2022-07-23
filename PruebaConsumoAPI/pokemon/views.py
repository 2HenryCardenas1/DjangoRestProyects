from django.shortcuts import render
from django.views.generic import TemplateView
from pokemon.services import get_droplets, get_pokemon,get_categorys


class Pokemon(TemplateView):
    template_name = 'index.html.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'droplets': get_droplets(),
        }
        return context


class GetPokemon(TemplateView):
    template_name = 'index.html.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'pokemons': get_pokemon(),
        }
        return context


class GetCategorys(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'categorys' : get_categorys()
        }

        return context