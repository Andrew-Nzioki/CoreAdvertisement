# Generated by Django 4.2.2 on 2023-06-13 07:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adcampaigns',
            name='advertisement_id',
            field=models.ManyToManyField(to='api.advertisement'),
        ),
        migrations.AddField(
            model_name='adcampaigns',
            name='vender',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='vender',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adimpresssions',
            name='ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.advertisement'),
        ),
        migrations.AlterField(
            model_name='adimpresssions',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.adcampaigns'),
        ),
        migrations.AlterField(
            model_name='adimpresssions',
            name='user_identifier',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
