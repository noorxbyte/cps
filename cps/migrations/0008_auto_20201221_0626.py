# Generated by Django 3.0.5 on 2020-12-21 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0007_daytankrecord_shift'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daytankrecord',
            old_name='final_mm',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='daytankrecord',
            old_name='initial_mm',
            new_name='initial',
        ),
    ]