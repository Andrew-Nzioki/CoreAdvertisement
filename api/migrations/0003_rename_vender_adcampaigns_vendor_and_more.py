# Generated by Django 4.2.2 on 2023-06-13 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_adcampaigns_advertisement_id_adcampaigns_vender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adcampaigns',
            old_name='vender',
            new_name='vendor',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='vender',
            new_name='vendor',
        ),
    ]
