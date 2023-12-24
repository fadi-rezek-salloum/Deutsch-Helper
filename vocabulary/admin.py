from django.contrib import admin

from .models import Composition, Sentence, Word

admin.site.register(Word)
admin.site.register(Composition)
admin.site.register(Sentence)
