from django.shortcuts import render, HttpResponse
from appmock import models


# ----------------- Home Page --------------------

def home(request) -> HttpResponse:
    return render(request, "appmock/home.html")


# ---------------- Function Based Views ----------


# ---------------- Class Based Views -------------


# TODO: Make the home page with two links to both function
# based view and class bases view index version
# Example -> home page with two links function based view, class based view
