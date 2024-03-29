# Generated by Django 3.2.24 on 2024-02-29 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_alter_location_locality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locations', to='catalogue.locality'),
        ),
    ]
