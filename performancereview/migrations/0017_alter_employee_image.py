# Generated by Django 5.0.6 on 2024-05-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0016_remove_employee_address_remove_employee_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/employee/'),
        ),
    ]
