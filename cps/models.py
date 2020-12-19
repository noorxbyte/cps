from django.db import models

# Create your models here.

class Engine(models.Model):

    class Meta:
        db_table = 'tblEngines'

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    details = models.CharField(max_length=255)



class Generator:

    class Meta:
        db_table = 'tblGenerators'

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    details = models.CharField(max_length=255)
    cap_kw = models.IntegerField()



class StorageTank:

    class Meta:
        db_table = 'tblStorageTanks'

    no = models.IntegerField(unique=True, db_index=True)
    max_mm = models.IntegerField()



class DayTank:

    class Meta:
        db_table = 'tblDayTanks'

    multiplier = models.IntegerField()
    max_mm = models.IntegerField()
    details = models.CharField(max_length=255)



class GenSet:

    class Meta:
        db_table = 'tblGenSets'

    no = models.IntegerField(unique=True, db_index=True)
    engine = models.ForeignKey(
        'Engine',
        on_delete=models.CASCADE
    )
    generator = models.ForeignKey(
        'Generator',
        on_delete=models.CASCADE
    )
    cap_kw = models.IntegerField()
    daytank = models.OneToOneField(
        'DayTank',
        on_delete = models.CASCADE
    )



class RunRecord:

    class Meta:
        db_table = 'tblRunRecords'

    class RunChoice(models.TextChoices):
        START = 'R'
        STOP = 'S'

    record_date = models.DateField()
    record_time = models.TimeField()
    genset = models.ForeignKey(
        'GenSet',
        on_delete=models.CASCADE
    )
    action = models.CharField(
        max_length=1,
        choices=RunChoice.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ProductionRecord:

    class Meta:
        db_table = 'tblProductionRecords'

    record_date = models.DateField()
    record_time = models.TimeField()
    genset = models.ForeignKey(
        'GenSet',
        on_delete=models.CASCADE
    )
    no = models.IntegerField(db_index=True)
    reading = models.IntegerField()
    ecc = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class StorageTankRecord:
    
    class Meta:
        db_table = 'tblStorageTankRecords'

    record_date = models.DateField()
    record_time = models.TimeField()
    storage_tank = models.ForeignKey(
        'StorageTank',
        on_delete=models.CASCADE
    )
    details = models.CharField(max_length=255)
    sounding = models.IntegerField()
    liters = models.IntegerField()
    diff = models.IntegerField()



class DayTankRecord:

    class Meta:
        db_table = 'tblDayTankRecords'

    record_date = models.DateField()
    record_time = models.TimeField()
    genset = models.ForeignKey(
        'GenSet',
        on_delete=models.CASCADE
    )
    daytank = models.ForeignKey(
        'DayTank',
        on_delete=models.CASCADE
    )
    no = models.IntegerField(db_index=True)
    is_daily_final = models.BooleanField(default=False)
    initial_mm = models.IntegerField()
    final_mm = models.IntegerField(
        default=None,
        blank=True,
        null=True
    )
    storage_tank_record = models.OneToOneField(
        'StorageTankRecord',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)