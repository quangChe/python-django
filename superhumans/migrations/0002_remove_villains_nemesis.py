# Generated by Django 2.2.1 on 2019-08-09 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superhumans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='villains',
            name='nemesis',
        ),
    ]
