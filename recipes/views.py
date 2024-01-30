from django.db import transaction

from django.shortcuts import render

from recipes.services import (add_product_to_recipe,
                              count_product_update,
                              recipes_without_product,
                              )


def add_product(request, **kwargs):
    """ Add or update ingredient in a recipe. """
    with transaction.atomic():
        result = add_product_to_recipe(**kwargs)
    context = {'result': result}
    return render(request, 'index.html', context)


def update_count_product(request, **kwargs):
    """ Update count ingredients. """
    with transaction.atomic():
        update_count = count_product_update(**kwargs)
    context = {'update_count': update_count}
    return render(request, 'index.html', context)


def show_recipes_without_product(request, **kwargs):
    """ Recipes without ingredient or quantity less than 10 grams. """
    recipes = recipes_without_product(**kwargs)
    context = {'recipes': recipes}
    return render(request, 'index.html', context)
