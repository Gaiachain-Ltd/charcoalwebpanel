# Generated by Django 2.2.7 on 2020-05-28 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbonizationending',
            name='ovens',
        ),
        migrations.AddField(
            model_name='oven',
            name='carbonization_ending',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ovens', to='entities.CarbonizationEnding', verbose_name='Carbonization Ending'),
        ),
        migrations.AlterField(
            model_name='package',
            name='type',
            field=models.CharField(choices=[('PLT', 'Plot'), ('HAR', 'Harvest'), ('TRK', 'Transport')], default='PLT', max_length=30, verbose_name='Type'),
        ),
    ]
