# Generated by Django 2.2.11 on 2020-03-29 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20200329_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='result',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]