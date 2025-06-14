from django.contrib import admin
from .models import Habito, RegistroHabito

@admin.register(Habito)
class HabitoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'frequencia', 'usuario')
    search_fields = ('nome',)
    list_filter = ('frequencia', 'usuario')

@admin.register(RegistroHabito)
class RegistroHabitoAdmin(admin.ModelAdmin):
    list_display = ('habito', 'data', 'feito')
    list_filter = ('feito', 'data')
    search_fields = ('habito__nome',)
