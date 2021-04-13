# Generated by Django 3.1.7 on 2021-04-12 21:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210413_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('DOB', models.DateField()),
            ],
        ),
    ]