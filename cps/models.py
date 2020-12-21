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
        else '{:04d}: {:f}'.format(self.max_mm, self.multiplier)



class Genset(models.Model):

    class Meta:
        db_table = 'tblGensets'
        unique_together = [['engine', 'generator']]

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

    def running(self):
        records = RunRecord.objects.filter(genset=self.id)\
            .order_by('-record_date', '-record_time')

        if records:
            if records[0].action == "START":
                return True

        return False



class RunRecord(models.Model):

    class Meta:
        db_table = 'tblRunRecords'

    class RunChoice(models.TextChoices):
        START = 'START'
        STOP = 'STOP'

    record_date = models.DateField()
    record_time = models.TimeField()
    genset = models.ForeignKey(
        'Genset',
        on_delete=models.CASCADE
    )
    action = models.CharField(
        max_length=5,
        choices=RunChoice.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.action == 'START':
            act = 'Started'
        elif self.action == 'STOP':
            act = 'Stopped'
        else:
            act = 'Error'

        return '{} {} at {} on {}'.format(
            act,
            self.genset,
            self.record_time,
            self.record_date
        )




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
    shift = models.CharField(max_length=1)
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
    shift = models.CharField(max_length=1)
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
    initial = models.IntegerField()
    final = models.IntegerField(
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