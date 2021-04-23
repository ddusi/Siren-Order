from django.shortcuts import render

from apps.logistics.models import Product
from .data import data


def home_view(request):
    context = {
        "dongdong": "1234",
        "Sinrim": data,
    }

    return render(request, "client/home.html", context)


def base_view(request):
    items = Product.objects.all()

    context = {"items": items}
    return render(request, "client/base.html", context)
