# Generated by Django 3.0.5 on 2020-11-30 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0002_remove_genset_cap_kva'),
    ]

    operations = [
        migrations.AddField(
            model_name='genset',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='genset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genset',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
