# Generated by Django 3.0.5 on 2020-12-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0008_auto_20201221_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagetank',
            name='in_use',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
