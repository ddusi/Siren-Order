from django.contrib import admin
from django.urls import path, include

from apps.client import views

home = [
    path("", views.home_view, name="home"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base_view, name="base"),
    path("home/", include(home)),
]
