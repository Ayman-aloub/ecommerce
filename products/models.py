from enum import unique
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.TextField(max_length=20,)
    description = models.TextField(max_length=70, default='')
    img = models.FileField(upload_to='./statics/images/categories')

    def __str__(self):
        return self.name


class product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.TextField(max_length=80,)
    name = models.TextField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField(default=0,)
    rate = models.FloatField(default=0, validators=[
                             MinValueValidator(1), MaxValueValidator(5)])
    numberofrate = models.IntegerField(default=0,)
    img = models.FileField(upload_to='./statics/images/products')

    def __str__(self):
        return self.name


class Rate(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='userRate')
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name='productRate')
    rate = models.IntegerField(null=False, validators=[
                               MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=70)

    class Meta:
        unique_together = ['user', 'product']


class Orders(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    date = models.DateTimeField(auto_now=True)
    totalprice = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='userOrder')
    products = models.ManyToManyField(
        product,  related_name='prodeuctOrder')
