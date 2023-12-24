from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls", namespace="base")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("vocabulary/", include("vocabulary.urls", namespace="vocabulary")),
]
