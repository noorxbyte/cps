# Generated by Django 3.0.5 on 2020-12-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0004_auto_20201221_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runrecord',
            name='action',
            field=models.CharField(choices=[('START', 'Start'), ('STOP', 'Stop')], max_length=5),
        ),
    ]