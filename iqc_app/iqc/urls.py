# iqc_app/iqc/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("iqc_app.core.urls", "core"), namespace="core")),
]
