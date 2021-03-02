# Generated by Django 3.1.6 on 2021-02-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210208_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hostel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='room_size',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='rooms',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.TextField(default=''),
        ),
    ]
