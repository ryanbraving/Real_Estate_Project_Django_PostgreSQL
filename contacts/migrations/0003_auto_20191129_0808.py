# Generated by Django 2.2.7 on 2019-11-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191129_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing',
            field=models.CharField(max_length=200),
        ),
    ]
