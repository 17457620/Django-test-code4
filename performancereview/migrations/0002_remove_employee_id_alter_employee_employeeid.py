# Generated by Django 5.0.6 on 2024-05-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeID',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]