# Generated by Django 2.2.7 on 2020-06-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0007_replantation_blockchain_batch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='reception_date',
            field=models.PositiveIntegerField(null=True, verbose_name='Reception date'),
        ),
    ]
