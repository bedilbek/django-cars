from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/car/makes/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'car_makes'
        ordering = ['name']


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/car/models/', null=True, blank=True)

    make = models.ForeignKey(CarMake, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'car_models'
        ordering = ['name']


class CarGeneration(models.Model):
    name = models.CharField(max_length=200)
    year_begin = models.PositiveIntegerField(null=True)
    year_end = models.PositiveIntegerField(null=True)

    model = models.ForeignKey(CarModel, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'car_generations'
        ordering = ['name']
