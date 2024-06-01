from django.contrib import admin
from .models import Remera

admin.site.register(Remera)

class RemeraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'get_talle_display', 'color', 'lisa', 'get_genero_display', 'precio')
    list_filter = ('marca', 'talle', 'color', 'lisa', 'genero')
    search_fields = ('nombre', 'marca', 'color')
