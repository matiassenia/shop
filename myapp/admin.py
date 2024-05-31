from django.contrib import admin
from .models import Remera

admin.site.register(Remera)

class RemeraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'get_talle_display', 'color', 'lisa', 'get_genero_display', 'precio')
    list_filter = ('marca', 'talle', 'color', 'lisa', 'genero')
    search_fields = ('nombre', 'marca', 'color')

'''
# Opcionalmente, si queremos mostrar un campo de imagen en la lista de administrador:
    def imagen_tag(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "No Image"
    imagen_tag.short_description = 'Imagen'
'''