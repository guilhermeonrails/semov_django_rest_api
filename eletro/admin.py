from django.contrib import admin
from eletro.models import Eletro

class EletroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'modelo','capacidade', 'ja_teve_conserto')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
    list_filter = ('ja_teve_conserto',)
    list_editable = ('ja_teve_conserto',)

admin.site.register(Eletro, EletroAdmin)