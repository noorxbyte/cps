from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from ..models import StorageTank, StorageTankRecord

def view(request, no):
    id = StorageTank.objects.get(no=no).id

    records = StorageTankRecord.objects.filter(storage_tank=id)\
        .order_by('record_date', 'record_time')

    no = '{:02d}'.format(no)
    in_use = StorageTank.objects.get(pk=id).in_use

    context = {
        "last_record": records[len(records) - 1],
        "in_use": in_use,
        "records": records,
        "no": no
    }
    return render(request, 'storagetank/view.html', context)