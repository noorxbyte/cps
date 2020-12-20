from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard.index, name='cps.dashboard'),
]
