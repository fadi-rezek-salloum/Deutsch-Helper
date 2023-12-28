import json

from django.contrib import messages
from django.db.models import Q
from django.forms import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .forms import CompositionCreationForm, SentenceCreationForm, WordCreationForm
from .mixins import SuperuserRequiredMixin
from .models import Composition, Sentence, Word


class CreateVocabularyWordView(SuperuserRequiredMixin, generic.CreateView):
    model = Word
    form_class = WordCreationForm
    template_name = "vocabulary/create_word.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            translation_en = form.cleaned_data["translation_en"]
            word, created = Word.objects.get_or_create(
                content=content, defaults={"translation_en": translation_en}
            )

            if created:
                word.translation_en = translation_en
                word.translation_ar = form.cleaned_data.get("translation_ar")
                word.notes = form.cleaned_data.get("notes")
                word.gender = form.cleaned_data.get("gender")
                word.category = form.cleaned_data.get("category")
                word.save()

            messages.success(request, "You have successfully created a new vocabulary word!")

        else:
            messages.error(request, "There is an error creating a new vocabulary word!")

        return redirect(request.path_info)


class UpdateVocabularyWordView(SuperuserRequiredMixin, generic.UpdateView):
    model = Word
    form_class = WordCreationForm
    template_name = "vocabulary/create_word.html"

    def form_valid(self, form):
        messages.success(self.request, "You have successfully updated this vocabulary word!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There is an error updating this vocabulary word!")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("vocabulary:update_word", args=(self.kwargs["pk"],))


class CreateVocabularyCompositionView(SuperuserRequiredMixin, generic.CreateView):
    model = Composition
    form_class = CompositionCreationForm
    template_name = "vocabulary/create_composition.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            translation_en = form.cleaned_data["translation_en"]
            composition, created = Composition.objects.get_or_create(
                content=content, defaults={"translation_en": translation_en}
            )

            if created:
                composition.translation_en = translation_en
                composition.translation_ar = form.cleaned_data.get("translation_ar")
                composition.notes = form.cleaned_data.get("notes")
                composition.save()

            messages.success(
                request, "You have successfully created a new vocabulary composition!"
            )

        else:
            messages.error(request, "There is an error creating a new vocabulary composition!")

        return redirect(request.path_info)


class UpdateVocabularyCompositionView(SuperuserRequiredMixin, generic.UpdateView):
    model = Composition
    form_class = CompositionCreationForm
    template_name = "vocabulary/create_composition.html"

    def form_valid(self, form):
        messages.success(
            self.request, "You have successfully updated this vocabulary composition!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There is an error updating this vocabulary composition!")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("vocabulary:update_composition", args=(self.kwargs["pk"],))


class CreateVocabularySentenceView(SuperuserRequiredMixin, generic.CreateView):
    model = Sentence
    form_class = SentenceCreationForm
    template_name = "vocabulary/create_sentence.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            translation_en = form.cleaned_data["translation_en"]
            sentence, created = Sentence.objects.get_or_create(
                content=content, defaults={"translation_en": translation_en}
            )

            if created:
                sentence.translation_en = translation_en
                sentence.translation_ar = form.cleaned_data.get("translation_ar")
                sentence.notes = form.cleaned_data.get("notes")
                sentence.save()

            messages.success(
                request, "You have successfully created a new vocabulary sentence!"
            )

        else:
            messages.error(request, "There is an error creating a new vocabulary sentence!")

        return redirect(request.path_info)


class UpdateVocabularySentenceView(SuperuserRequiredMixin, generic.UpdateView):
    model = Sentence
    form_class = SentenceCreationForm
    template_name = "vocabulary/create_sentence.html"

    def form_valid(self, form):
        messages.success(
            self.request, "You have successfully updated this vocabulary sentence!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There is an error updating this vocabulary sentence!")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("vocabulary:update_sentence", args=(self.kwargs["pk"],))


@method_decorator(csrf_exempt, name="dispatch")
class ListVocabularyWordView(generic.ListView):
    model = Word
    template_name = "vocabulary/list_word.html"

    def post(self, request):
        q = json.loads(request.body).get("q", None)

        qs = self.get_queryset()

        if q:
            qs = qs.filter(Q(content__icontains=q) | Q(translation_en__icontains=q))

        data = []

        for item in qs:
            item_dict = model_to_dict(item)
            item_dict["category"] = item.get_category_display()
            item_dict["gender"] = item.get_gender_display()
            data.append(item_dict)

        return JsonResponse(data, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class ListVocabularyCompositionView(generic.ListView):
    model = Composition
    template_name = "vocabulary/list_composition.html"

    def post(self, request):
        q = json.loads(request.body).get("q", None)

        qs = self.get_queryset()

        if q:
            qs = qs.filter(Q(content__icontains=q) | Q(translation_en__icontains=q))

        return JsonResponse(list(qs.values()), safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class ListVocabularySentenceView(generic.ListView):
    model = Sentence
    template_name = "vocabulary/list_sentence.html"

    def post(self, request):
        q = json.loads(request.body).get("q", None)

        qs = self.get_queryset()

        if q:
            qs = qs.filter(Q(content__icontains=q) | Q(translation_en__icontains=q))

        return JsonResponse(list(qs.values()), safe=False)
