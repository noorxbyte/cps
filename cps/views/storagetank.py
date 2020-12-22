from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from ..models import StorageTank, StorageTankRecord

def view(request, id):
    records = StorageTankRecord.objects.filter(storage_tank=id)\
        .order_by('record_date', 'record_time')

    no = '{:02d}'.format(StorageTank.objects.get(pk=id).no)

    context = {
        "last_record": records[len(records) - 1],
        "records": records,
        "no": no
    }
    return render(request, 'storagetank/view.html', context)