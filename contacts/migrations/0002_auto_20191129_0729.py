# Generated by Django 2.2.7 on 2019-11-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
