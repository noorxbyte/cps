# Generated by Django 3.0.5 on 2020-12-24 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0009_storagetank_in_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageTankData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sounding', models.IntegerField()),
                ('liters', models.IntegerField()),
                ('storage_tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cps.StorageTank')),
            ],
            options={
                'db_table': 'tblStorageTankData',
            },
        ),
    ]
