# Generated by Django 5.0.3 on 2024-03-20 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20240319_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.show')),
            ],
        ),
    ]
