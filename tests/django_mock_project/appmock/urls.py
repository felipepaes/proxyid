from django.urls import path
from appmock import views


urlpatterns = [
    path("", views.home, name="home"),


    # function based views
    path("function/", views.person_list, name="function-person-list"),

    path("function/<pk>/int-person/",
         views.person_int_pk_detail,
         name="function-person-int-detail"),

    path("function/<pk>/uuid-person/",
         views.person_uuid_pk_detail,
         name="function-person-uuid-detail"),


    # clas based views
    path("class/", views.PersonListView.as_view(), name="class-person-list"),

    path("class/<pk>/int-person/",
         views.PersonIntegerDetailView.as_view(),
         name="class-person-int-detail"),

    path("class/<pk>/uuid-person/",
         views.PersonUUIDDetailView.as_view(),
         name="class-person-uuid-detail"),


    # custom url arg class based views
    path("custom/<boomshakalaka>/int-person/",
         views.CustomPersonIntegerDetailView.as_view(),
         name="custom-person-int-detail"),

    path("custom/<boomshakalaka>/uuid-person/",
         views.CustomPersonUUIDDetailView.as_view(),
         name="custom-person-uuid-detail"),
]
