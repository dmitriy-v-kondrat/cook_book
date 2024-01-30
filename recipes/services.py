
from django.db.models import F, Q, QuerySet

from recipes.models import Ingredient, WeightIngredient, Recipe


def add_product_to_recipe(**kwargs: int) -> str:
    """
    Adds the specified product
    with the specified weight to the specified recipe.
    If the recipe already contains such a product,
    the function updates its weight in that recipe
     to the specified value.

    :param kwargs: recipe_id: id;
                   ingredient_id: id;
                   weight: id;
    :return: str
    """
    query = WeightIngredient.objects\
        .filter(recipe_id=kwargs.get('recipe_id'),
                ingredient_id=kwargs.get('ingredient_id')
                )

    if query:
        query.update(weight=kwargs.get('weight'))

        return 'Ingredient updated'
    else:
        WeightIngredient.objects.create(recipe_id=kwargs.get('recipe_id'),
                                        ingredient_id=kwargs.get(
                                                'ingredient_id'),
                                        weight=kwargs.get('weight')
                                        )
        return 'Ingredient added'


def count_product_update(**kwargs: int) -> int:
    """
    Increments by one
    the quantity of each product
    included in the recipe.
    Returns the count of updated products.

    :param kwargs: recipe_id: id;
    :return: int
    """
    update_count = Ingredient.objects \
        .filter(weights__recipe=kwargs.get('recipe_id')) \
        .update(used=F('used') + 1)

    return update_count


def recipes_without_product(**kwargs: int) -> QuerySet:
    """
    Returns a queryset recipes
    in which the specified product is
    either absent or present in a quantity less than 10 grams.

    :param kwargs: ingredient_id: id;
    :return: QuerySet
    """

    recipes = Recipe.objects \
        .filter(
            ~Q(weight_ingredients__ingredient_id=kwargs.get('ingredient_id')) |
            Q(weight_ingredients__weight__lt=10,
              weight_ingredients__ingredient_id=kwargs.get('ingredient_id')
              )
            ).distinct()

    return recipes
