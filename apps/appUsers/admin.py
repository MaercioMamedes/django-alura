from django.contrib import admin
from .models import UserApp

"""module responsible for configuring the views of application models within the App admin"""

class ListingUser(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id','user')
    #search_fields = ('name',)
    list_per_page = 5


admin.site.register(UserApp, ListingUser)
