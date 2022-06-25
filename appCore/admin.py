from django.contrib import admin
from .models import *


class ListingRecipes(admin.ModelAdmin):
    list_display = ('id', 'name_recipe', 'category')
    list_display_links = ('id', 'name_recipe', 'category')
    search_fields = ('name_recipe',)
    list_filter = ('category',)
    list_per_page = 5


admin.site.register(Recipe, ListingRecipes)
