# Generated by Django 2.1.2 on 2018-11-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20181121_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='smscode',
            name='udid',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]