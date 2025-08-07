from django.contrib import admin

# Register your models here.
from .models import Categoria, Desafio, Flashcard, FlashcardDesafio

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(FlashcardDesafio)
admin.site.register(Desafio)