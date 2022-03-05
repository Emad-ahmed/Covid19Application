from django.urls import path
from covid19App.views import index

urlpatterns = [
    path("", index, name="home")
]
