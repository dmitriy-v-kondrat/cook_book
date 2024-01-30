from django.db import models


class Ingredient(models.Model):
    """
    Food product.
    """

    name = models.CharField(max_length=255,
                            unique=True
                            )
    used = models.PositiveIntegerField(blank=True,
                                       default=0,
                                       verbose_name='How'
                                                    ' many'
                                                    ' times'
                                                    ' was'
                                                    ' it'
                                                    ' used'
                                       )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Dish recipe.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WeightIngredient(models.Model):
    """
    Weight ingredient from a recipe.
    """
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='weight_ingredients'
                               )
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   related_name='weights'
                                   )
    weight = models.PositiveIntegerField(verbose_name='weight gram')
