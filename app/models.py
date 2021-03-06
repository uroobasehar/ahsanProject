# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    category = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    product_image = models.ImageField(max_length=255,  default="/static/assets/img/image-placeholder.jpg", null=True, blank=True)
    
    class Meta:
        db_table = 'product'

class product_category(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    parent_category = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category_image = models.ImageField(max_length=255,  default="/static/assets/img/image-placeholder.jpg", null=True, blank=True)

    class Meta:
        db_table = 'product_category'

class review(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    product_id = models.IntegerField()
    description = models.CharField(max_length=100)
    reviewer_id = models.IntegerField()
    
    class Meta:
        db_table = 'review'

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'user'