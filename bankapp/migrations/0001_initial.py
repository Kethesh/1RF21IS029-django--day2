# Generated by Django 5.0.6 on 2024-06-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('aadhar_no', models.CharField(max_length=12, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('account_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
