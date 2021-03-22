from django.shortcuts import render, HttpResponse
from django.views import generic

from appmock import models

from proxyid.encoding import decode
from proxyid.mixins import ProxyidMixin


# ----------------- Home Page --------------------


def home(request) -> HttpResponse:
    return render(request, "appmock/home.html")


# ---------------- Function Based Views ----------

def person_list(request) -> HttpResponse:
    int_persons = models.PersonIntegerPK.objects.all()
    uuid_persons = models.PersonUUIDPK.objects.all()
    context = {
        "int_persons": int_persons,
        "uuid_persons": uuid_persons,
    }
    return render(request, "appmock/person_list.html", context)


def person_int_pk_detail(request, pk) -> HttpResponse:
    decoded_pk = decode(pk)
    person = models.PersonIntegerPK.objects.get(pk=decoded_pk)
    context = {"person": person}
    return render(request, "appmock/person_detail.html", context)


def person_uuid_pk_detail(request, pk) -> HttpResponse:
    decoded_pk = decode(pk)
    person = models.PersonUUIDPK.objects.get(pk=decoded_pk)
    context = {"person": person}
    return render(request, "appmock/person_detail.html", context)


# ---------------- Class Based Views -------------


class PersonListView(generic.TemplateView):
    template_name = "appmock/person_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["int_persons"] = models.PersonIntegerPK.objects.all()
        context["uuid_persons"] = models.PersonUUIDPK.objects.all()
        return context


class PersonIntegerDetailView(ProxyidMixin, generic.DetailView):
    template_name = "appmock/person_detail.html"
    model = models.PersonIntegerPK
    context_object_name = "person"


class PersonUUIDDetailView(ProxyidMixin, generic.DetailView):
    template_name = "appmock/person_detail.html"
    model = models.PersonUUIDPK
    context_object_name = "person"
