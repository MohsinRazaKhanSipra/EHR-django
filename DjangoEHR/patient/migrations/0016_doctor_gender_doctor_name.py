# Generated by Django 4.0.1 on 2023-09-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_alter_doctor_bio_alter_doctor_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
