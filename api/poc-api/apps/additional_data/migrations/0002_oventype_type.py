# Generated by Django 2.2.7 on 2020-06-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oventype',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Custom'), (2, 'Fixed')], default=1),
        ),
    ]
