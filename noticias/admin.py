from django.contrib import admin
from noticias.models import Noticia, Rubrica

class RubricaAdmin(admin.ModelAdmin):
    pass

class NoticiaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Rubrica, RubricaAdmin)