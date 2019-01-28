from django.contrib import admin
from .models import Animal, Equipement


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'RACE', 'TYPE', 'ETAT', 'LIEU')


class EquipementAdmin(admin.ModelAdmin):
    list_display = ('equipement', 'DISPO')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Equipement, EquipementAdmin)

# Register your models here.
