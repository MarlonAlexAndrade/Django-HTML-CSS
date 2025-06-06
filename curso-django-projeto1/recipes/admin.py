
from django.contrib import admin

from .models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

# Segunda forma de fazer
# admin.site.register(Category, CategoryAdmin)