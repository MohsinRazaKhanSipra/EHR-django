# Generated by Django 4.0.1 on 2023-09-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
