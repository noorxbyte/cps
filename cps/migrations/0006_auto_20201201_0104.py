# Generated by Django 3.0.5 on 2020-11-30 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0005_runrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runrecord',
            name='genset_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cps.Genset'),
        ),
        migrations.CreateModel(
            name='DayTankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('multiplier', models.FloatField()),
                ('genset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cps.Genset')),
            ],
        ),
    ]
