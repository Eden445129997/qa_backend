from django.http import HttpResponse
from django.shortcuts import render

from .ODBC import odbc

# Create your controller here.

def show_tables(request):
    table = request.GET.get("table")
    db = odbc(table)

    response = db.selectSQL("show tables")

    return HttpResponse(response)

def template(request):
    return render(request,"index.html")