# Generated by Django 2.2.7 on 2020-07-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_data', '0003_auto_20200721_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='oventype',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='treespecie',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='village',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='oventype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.RenameField(
            model_name='parcel',
            old_name='code',
            new_name='name',
        ),
    ]