from django.contrib import admin

from .models import Genset, RunRecord, DayTankInfo

# Register your models here.

admin.site.register(Genset)
admin.site.register(RunRecord)
admin.site.register(DayTankInfo)
