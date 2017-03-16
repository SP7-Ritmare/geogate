from django.contrib import admin

from .models import Node, Catalog

class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'baseurl', 'harvesting_url', 'harvesting_type')

admin.site.register(Node, NodeAdmin)

admin.site.register(Catalog)
