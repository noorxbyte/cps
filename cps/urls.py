from django.urls import path

from . import views

urlpatterns = [
    path('', views.home.dashboard, name='cps.dashboard'),
]
