# Generated by Django 3.0.5 on 2020-12-20 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0003_auto_20201220_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runrecord',
            old_name='Genset',
            new_name='genset',
        ),
    ]
