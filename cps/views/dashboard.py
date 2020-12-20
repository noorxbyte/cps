from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from ..models import Genset

@login_required
def index(request):
    context = {
        "gensets": Genset.objects.all().filter(operational=True)
    }
    return render(request, 'dashboard.html', context)