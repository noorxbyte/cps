from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard.index, name='cps.dashboard'),

    path('daytanks/', views.daytank.index, name='cps.daytanks.index'),

    path('genset/<int:genset_no>/start', views.run.start, name='cps.genset.start'),
    path('genset/<int:genset_no>/stop', views.run.stop, name='cps.genset.stop'),

    # Add refill record by genset no
    path('genset/<int:genset_no>/daytank/refill', views.daytank.refill, name='cps.genset.daytank.refill'),
    # Add refill record by daytank id
    path('daytank/id/<int:daytank_id>/refill', views.daytank.refill, name='cps.daytank.refill'),

    # Day tank view by id
    path('daytank/id/<int:daytank_id>', views.daytank.view, name='cps.daytanks.view'),
    # Day tank view by genset no
    path('genset/<int:genset_no>/daytank', views.daytank.view, name='cps.genset.daytank.view'),

    # Storage tank view by no
    path('storagetank/<int:no>/', views.storagetank.view, name='cps.storagetanks.view'),
]
