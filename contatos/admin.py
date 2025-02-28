from django.contrib import admin
from .models import Contato

class AdminContato(admin.ModelAdmin):
   search_fields = ['nome','sobrenome']
   list_display = ['id', 'nome', 'sobrenome', 'data_criacao', 'ativo']
   list_display_links = ['nome']
   list_filter = ['ativo']
   
admin.site.register(Contato, AdminContato)

