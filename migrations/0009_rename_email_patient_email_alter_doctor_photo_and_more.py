# Generated by Django 5.0 on 2024-07-09 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproj', '0008_doctor_specialist_alter_doctor_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Email',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='docimage'),
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApointmentDate', models.DateField()),
                ('ApointmentTime', models.TimeField()),
                ('patient', models.PositiveIntegerField()),
                ('Status', models.CharField(max_length=255, null=True)),
                ('patient_phone', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=255)),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finalproj.doctor')),
            ],
        ),
    ]
