from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submissions/", views.submissions_list, name="submissions_list"),
]
