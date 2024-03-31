# Generated by Django 5.0.2 on 2024-03-26 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_orderitem_order_ordered_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('langue', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AlterModelTable(
            name='artisttype',
            table='artiste_type',
        ),
        migrations.CreateModel(
            name='ArtistTypeShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_type_show', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artiste_type_show', to='catalogue.artist')),
                ('show', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artiste_type_show', to='catalogue.show')),
            ],
            options={
                'db_table': 'artiste_type_show',
            },
        ),
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations', to='catalogue.location')),
                ('show', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations', to='catalogue.show')),
            ],
            options={
                'db_table': 'representations',
            },
        ),
        migrations.CreateModel(
            name='RoleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role_user', to='catalogue.role')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role_user', to='catalogue.user')),
            ],
            options={
                'db_table': 'role_user',
            },
        ),
        migrations.CreateModel(
            name='RepresentationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations_user', to='catalogue.representation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='representations_user', to='catalogue.user')),
            ],
            options={
                'db_table': 'representation_user',
            },
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
