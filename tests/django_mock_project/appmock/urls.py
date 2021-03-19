from django.urls import path
from appmock import views

urlpatterns = [
    path('', views.home, name="home"),
]
