from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)

    #crud-web methods
    #create/insert/add-POST
    #restrive/fetch/GET
    #update/edit/PUT
    #delete/remove/DELETE
