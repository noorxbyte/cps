from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from ..models import DayTank, DayTankRecord, StorageTankRecord, Genset

def view(request, daytank_id=None, genset_no=None):
    id = daytank_id if daytank_id else\
        Genset.objects.get(no=genset_no).daytank.id if genset_no else None

    records = DayTankRecord.objects.filter(daytank=id)\
        .order_by('record_date', 'record_time')

    no = '{:02d}'.format(DayTank.objects.get(pk=id).genset.no)

    for record in records:
        record.initial_liters = round(record.daytank.multiplier * record.initial)
        record.final_liters = round(record.daytank.multiplier * record.final)\
            if record.final else None

    print(records)

    context = {
        "records": records,
        "no": no
    }
    return render(request, 'daytank/view.html', context)

def refill(request, daytank_id=None, genset_no=None):
    id = daytank_id if daytank_id else\
        Genset.objects.get(no=genset_no).daytank.id if genset_no else None

    context = {
        "no": '{:02d}'.format(DayTank.objects.get(pk=id).genset.no)
    }
    
    return render(request, 'daytank/refill.html', context)

def index(request):
    context = {
        "gensets": Genset.objects.all().filter(operational=True)
    }
    return render(request, 'dashboard.html', context)