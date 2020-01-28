# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product = models.CharField(max_length =300)

    def save_pro(self):
        self.save()   

    @classmethod
    def search_by_product(cls,search):
        products = cls.objects.filter(products__product__icontains=search)
        return products

    def __str__(self):
        return self.product

class Add(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    nid=models.CharField(max_length=300)
    fone=models.CharField(max_length=300)

    def save_custo(self):
        self.save()
                      
    def dele(self):
        self.delete() 

    @classmethod
    def update(cls,id):
        customer = cls.objects.filter(id=id).update(id=id)
        return customer   

    def __str__(self):
        return self.name

