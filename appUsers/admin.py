from django.contrib import admin
from .models import User


class ListingUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name',)
    list_per_page = 5


admin.site.register(User, ListingUser)
