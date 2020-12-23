from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from ..models import StorageTank, StorageTankRecord

def view(request, no):
    records = StorageTankRecord.objects.filter(storage_tank=no)\
        .order_by('record_date', 'record_time')

    no = '{:02d}'.format(StorageTank.objects.get(pk=no).no)

    context = {
        "last_record": records[len(records) - 1],
        "records": records,
        "no": no
    }
    return render(request, 'storagetank/view.html', context)