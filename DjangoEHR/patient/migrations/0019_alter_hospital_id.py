# Generated by Django 4.2.5 on 2023-09-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0018_hospital_doctor_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
