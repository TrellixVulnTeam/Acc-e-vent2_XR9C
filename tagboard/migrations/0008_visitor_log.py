# Generated by Django 2.2.4 on 2019-08-07 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0007_event_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor_Log',
            fields=[
                ('uid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('attempt', models.BooleanField()),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagboard.MID')),
            ],
        ),
    ]