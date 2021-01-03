from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime

# Create your views here.

from ..models import RunRecord, Genset

def start(request, genset_no=None):
    if __start_valid(genset_no, request.POST):
        r = RunRecord()
        r.record_date = datetime.date.today()
        r.record_time = request.POST.get('start_time')
        r.genset = Genset.objects.get(no=genset_no)
        r.action = 'START'
        r.save()

        messages.add_message(request, messages.SUCCESS, 'Genset {:02d} started successfully!'.format(genset_no))

    messages.add_message(request, messages.WARNING, 'Genset {:02d} couldn\'t be started!'.format(genset_no))
    return redirect('cps.dashboard')



def stop(request, genset_no=None):
    if __stop_valid(genset_no, request.POST):
        r = RunRecord()
        r.record_date = datetime.date.today()
        r.record_time = request.POST.get('stop_time')
        r.genset = Genset.objects.get(no=genset_no)
        r.action = 'STOP'
        r.save()

        messages.add_message(request, messages.SUCCESS, 'Genset {:02d} stopped successfully!'.format(genset_no))

    messages.add_message(request, messages.WARNING, 'Genset {:02d} couldn\'t be stopped!'.format(genset_no))
    return redirect('cps.dashboard')



def __start_valid(genset_no, req):
    return False



def __stop_valid(genset_no, req):
    return True