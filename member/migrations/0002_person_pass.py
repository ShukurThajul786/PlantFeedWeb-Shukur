# Generated by Django 4.2.4 on 2023-09-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Pass',
            field=models.CharField(default='', max_length=150),
        ),
    ]
