# Generated by Django 5.0.6 on 2024-07-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproj', '0002_alter_hospital_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='Rooms',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
