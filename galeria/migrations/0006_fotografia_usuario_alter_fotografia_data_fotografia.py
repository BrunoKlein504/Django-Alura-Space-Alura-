# Generated by Django 5.1.6 on 2025-03-07 14:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_data_fotografia_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 7, 11, 36, 40, 567166)),
        ),
    ]
