from django.urls import path

from . import views

app_name = "vocabulary"

urlpatterns = [
    path("word/create/", views.CreateVocabularyWordView.as_view(), name="create_word"),
    path("word/update/<pk>/", views.UpdateVocabularyWordView.as_view(), name="update_word"),
    path("word/list/", views.ListVocabularyWordView.as_view(), name="list_word"),
    path(
        "composition/create/",
        views.CreateVocabularyCompositionView.as_view(),
        name="create_composition",
    ),
    path(
        "composition/update/<pk>/",
        views.UpdateVocabularyCompositionView.as_view(),
        name="update_composition",
    ),
    path(
        "composition/list/",
        views.ListVocabularyCompositionView.as_view(),
        name="list_composition",
    ),
    path(
        "sentence/create/",
        views.CreateVocabularySentenceView.as_view(),
        name="create_sentence",
    ),
    path(
        "sentence/update/<pk>/",
        views.UpdateVocabularySentenceView.as_view(),
        name="update_sentence",
    ),
    path("sentence/list/", views.ListVocabularySentenceView.as_view(), name="list_sentence"),
]
