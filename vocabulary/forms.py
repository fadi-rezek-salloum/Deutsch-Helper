from django import forms

from .models import Composition, Sentence, Word


class WordCreationForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = "__all__"


class CompositionCreationForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = "__all__"


class SentenceCreationForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = "__all__"
