from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.autotest_login),
    path('logout/',views.autotest_logout),
    path('home/',views.home),
]