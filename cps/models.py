from django.db import models

# Create your models here.

class Genset(models.Model):
    available = models.BooleanField(default=True)
    number = models.IntegerField(unique=True) 
    serial_number = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    cap_kw = models.IntegerField()

    def __str__(self):
        return 'Genset {}'.format(self.number)



class RunRecord(models.Model):

    class Action(models.TextChoices):
        START = 'START'
        STOP = 'STOP'

    genset_id = models.ForeignKey(
        'Genset',
        on_delete=models.CASCADE
    )
    record_date = models.DateField()
    record_time = models.TimeField()
    action = models.CharField(
        max_length=5,
        choices=Action.choices
    )

    def __str__(self):
        return '{} {} on {} at {}'.format(
            self.action,
            self.genset_id,
            self.record_date,
            self.record_time,
        )



class DayTankInfo(models.Model):
    genset_id = models.OneToOneField(
        'Genset',
        on_delete=models.CASCADE,
    )
    capacity = models.IntegerField()
    multiplier = models.FloatField()

    def __str__(self):
        return 'Day tank for {}'.format(self.genset_id)