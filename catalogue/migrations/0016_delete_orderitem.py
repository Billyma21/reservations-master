# Generated by Django 5.0.3 on 2024-03-26 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_orderitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]