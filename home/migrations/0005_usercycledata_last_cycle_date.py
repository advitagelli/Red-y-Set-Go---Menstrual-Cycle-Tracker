# Generated by Django 5.1.2 on 2024-10-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_usercycledata_predicted_cycle_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercycledata',
            name='last_cycle_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
