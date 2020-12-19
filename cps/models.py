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
    details = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return '{} {} (SN: {})'.format(
            self.make,
            self.model,
            self.serial_number
        )



class Generator(models.Model):

    class Meta:
        db_table = 'tblGenerators'

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    details = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    cap_kw = models.IntegerField()

    def __str__(self):
        return '{} {} (SN: {})'.format(
            self.make,
            self.model,
            self.serial_number
        )



class StorageTank(models.Model):

    class Meta:
        db_table = 'tblStorageTanks'

    no = models.IntegerField(unique=True, db_index=True)
    max_mm = models.IntegerField()

    def __str__(self):
        return 'Storage Tank {:02d}'.format(self.no)



class DayTank(models.Model):

    class Meta:
        db_table = 'tblDayTanks'

    multiplier = models.FloatField()
    max_mm = models.IntegerField()
    details = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Day Tank {:02d}'.format(self.genset.no) \
        if hasattr(self, 'genset') \
        else 'DT: {}'.format(self.details)



class Genset(models.Model):

    class Meta:
        db_table = 'tblGensets'

    no = models.IntegerField(unique=True, db_index=True)
    operational = models.BooleanField(default=True)
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
        on_delete = models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'DEG {:02d}'.format(self.no)



class RunRecord(models.Model):

    class Meta:
        db_table = 'tblRunRecords'

    class RunChoice(models.TextChoices):
        START = 'R'
        STOP = 'S'

    record_date = models.DateField()
    record_time = models.TimeField()
    Genset = models.ForeignKey(
        'Genset',
        on_delete=models.CASCADE
    )
    action = models.CharField(
        max_length=1,
        choices=RunChoice.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ProductionRecord(models.Model):

    class Meta:
        db_table = 'tblProductionRecords'

    record_date = models.DateField()
    record_time = models.TimeField()
    Genset = models.ForeignKey(
        'Genset',
        on_delete=models.CASCADE
    )
    no = models.IntegerField(db_index=True)
    reading = models.IntegerField()
    ecc = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class StorageTankRecord(models.Model):
    
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



class DayTankRecord(models.Model):

    class Meta:
        db_table = 'tblDayTankRecords'

    record_date = models.DateField()
    record_time = models.TimeField()
    Genset = models.ForeignKey(
        'Genset',
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