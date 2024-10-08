from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("letting/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
]
