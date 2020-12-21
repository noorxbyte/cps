from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Engine)
admin.site.register(Generator)
admin.site.register(Genset)
admin.site.register(StorageTank)
admin.site.register(DayTank)

admin.site.register(RunRecord)