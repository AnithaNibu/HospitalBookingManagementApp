# Generated by Django 4.1.4 on 2023-01-01 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('patient_phone', models.CharField(max_length=10)),
                ('patient_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.doctors')),
            ],
        ),
    ]
