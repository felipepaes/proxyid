from django.conf.urls import url
from appmock import views


urlpatterns = [
    url(r"^$", views.home, name="home"),


    url(r"^function/$", views.person_list, name="function-person-list"),

    url(r"^function/(?P<pk>[a-zA-Z0-9]+)/int-person/$",
         views.person_int_pk_detail,
         name="function-person-int-detail"),

    url(r"^function/(?P<pk>[a-zA-Z0-9]+)/uuid-person/$",
         views.person_uuid_pk_detail,
         name="function-person-uuid-detail"),


    url(r"^class/$", views.PersonListView.as_view(), name="class-person-list"),

    url(r"^class/(?P<pk>[a-zA-Z0-9]+)/int-person/$",
         views.PersonIntegerDetailView.as_view(),
         name="class-person-int-detail"),

    url(r"^class/(?P<pk>[a-zA-Z0-9]+)/uuid-person/$",
         views.PersonUUIDDetailView.as_view(),
         name="class-person-uuid-detail"),
]
