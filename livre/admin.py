from django.contrib import admin
from .models import Livre
# Register your models here.


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description',
                    'date_publication', 'image', 'auteur')

    list_filter = (
        'auteur',

    )

    ordering = ['titre']
