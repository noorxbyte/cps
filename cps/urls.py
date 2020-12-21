from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard.index, name='cps.dashboard'),

    path('daytanks/', views.daytank.index, name='cps.daytanks.index'),
    path('daytank/<int:id>/', views.daytank.view, name='cps.daytanks.view'),

    path('storagetank/<int:id>/', views.storagetank.view, name='cps.storagetanks.view'),
]
