# Generated by Django 2.2.4 on 2019-08-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0010_event_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]