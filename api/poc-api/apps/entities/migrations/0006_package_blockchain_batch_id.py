# Generated by Django 2.2.7 on 2020-06-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0005_auto_20200605_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='blockchain_batch_id',
            field=models.CharField(blank=True, max_length=128, verbose_name='Blockchain Batch ID'),
        ),
    ]
