#coding=utf-8
from django.http import HttpResponse
from django.urls import path
from . import views

def test(request):
    return HttpResponse("hhhh")

urlpatterns = [
    path('tables/',views.show_tables),
    path('test/',test),
    path('template/',views.template),
]