# Generated by Django 5.0.7 on 2024-07-20 11:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('shirt', models.CharField(blank=True, max_length=255, null=True)),
                ('pant', models.CharField(blank=True, max_length=255, null=True)),
                ('kurtha', models.CharField(blank=True, max_length=255, null=True)),
                ('others', models.CharField(blank=True, max_length=255, null=True)),
                ('shirt_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pant_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('customer_image', models.ImageField(blank=True, null=True, upload_to='customer_images/')),
                ('shirt_image', models.ImageField(blank=True, null=True, upload_to='shirt_images/')),
                ('pant_image', models.ImageField(blank=True, null=True, upload_to='pant_images/')),
            ],
        ),
    ]
