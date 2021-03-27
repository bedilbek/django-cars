# Generated by Django 3.1.7 on 2021-03-27 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(null=True, upload_to='images/car/makes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'car_makes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/car/models/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car.carmake')),
            ],
            options={
                'db_table': 'car_models',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CarGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_begin', models.PositiveIntegerField(null=True)),
                ('year_end', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car.carmodel')),
            ],
            options={
                'db_table': 'car_generations',
                'ordering': ['name'],
            },
        ),
    ]
