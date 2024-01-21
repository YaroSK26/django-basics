from django.urls import path
from . import views

urlpatterns = [
    path("hello-world", views.hello_world, name="hello-world"),
    path("hello-school", views.hello_school, name="hello-school"),
]
