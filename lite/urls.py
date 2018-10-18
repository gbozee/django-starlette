from django.urls import path
from django.http import JsonResponse


def hello_world(request):
    return JsonResponse({"hello": "world"})


def new_method(request):
    return JsonResponse({"new": "method"})

urlpatterns = [
    path("", hello_world, name="hello_world"),
    path("new-method", new_method, name="new_method"),
]

