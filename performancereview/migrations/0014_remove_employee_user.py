# Generated by Django 5.0.6 on 2024-05-23 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performancereview', '0013_delete_category_delete_customer_delete_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]
