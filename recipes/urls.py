
from django.urls import path

from recipes.views import (add_product,
                           show_recipes_without_product,
                           update_count_product,
                           )

urlpatterns = [
    path('add-product-to-recipe/<int:recipe_id>/'
         '<int:ingredient_id>/<int:weight>/',
         add_product
         ),

    path('update-count-product/<int:recipe_id>/',
         update_count_product
         ),

    path('show-recipes-without-product/<int:ingredient_id>/',
         show_recipes_without_product
         ),
    ]