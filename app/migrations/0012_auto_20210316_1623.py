# Generated by Django 3.1.6 on 2021-03-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210312_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hostel',
            field=models.CharField(max_length=100),
        ),
    ]
