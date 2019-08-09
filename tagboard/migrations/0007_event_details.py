# Generated by Django 2.2.4 on 2019-08-07 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0006_location_mid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duration', models.CharField(max_length=20)),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagboard.MID')),
            ],
        ),
    ]
