from django.db import models


class Word(models.Model):
    class CATEGORY_CHOICES(models.TextChoices):
        NAME = "NA", "Nomen"
        ADJECTIVE = "AD", "Adjektive"
        VERB = "VE", "Verben"
        MODAL_VERB = "MVE", "Modal Verben"
        INTERJEKTIONEN = "INTER", "Interjektionen"
        ADVERB = "ADV", "Adverb"
        PRONOMEN = "PRO", "Pronomen"
        FRAGEPRONOMEN = "FPRO", "Fragepronomen"

    class GENDER_CHOICES(models.TextChoices):
        M = "M", "Maskulin"
        F = (
            "F",
            "Feminin",
        )
        N = "N", "Neutral"

    content = models.CharField(max_length=70)

    f_form = models.CharField("Feminin (Form)", max_length=70, null=True, blank=True)
    p_form = models.CharField("Plural (Form)", max_length=70, null=True, blank=True)

    category = models.CharField(
        max_length=5, choices=CATEGORY_CHOICES.choices, null=True, blank=True
    )
    gender = models.CharField(
        max_length=3, choices=GENDER_CHOICES.choices, null=True, blank=True
    )

    translation_en = models.CharField(max_length=70)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content} -> {self.translation_en}"


class Composition(models.Model):
    content = models.CharField(max_length=150)

    translation_en = models.CharField(max_length=150)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content} -> {self.translation_en}"


class Sentence(models.Model):
    content = models.CharField(max_length=150)

    translation_en = models.CharField(max_length=150)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content} -> {self.translation_en}"
