# Generated by Django 3.2.12 on 2022-07-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0093_auto_20220711_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='assets',
        ),
        migrations.AddField(
            model_name='systemuser',
            name='assets',
            field=models.ManyToManyField(blank=True, related_name='system_users', to='assets.Asset', verbose_name='Assets'),
        ),
    ]
