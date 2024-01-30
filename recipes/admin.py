from django.contrib import admin

from recipes.models import (Ingredient,
                            Recipe,
                            WeightIngredient
                            )


class WeightIngredientInline(admin.TabularInline):
    model = WeightIngredient
    extra = 0
    fields = ('ingredient', 'weight')


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', 'id')
    readonly_fields = ('used',)
    show_full_result_count = False


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        WeightIngredientInline
        ]
    list_display = ('name', 'id')
    model = Recipe
    show_full_result_count = False


class WeightIngredientAdmin(admin.ModelAdmin):
    model = WeightIngredient


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(WeightIngredient, WeightIngredientAdmin)
