from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)
class student(models.Model):
    Name=models.CharField(max_length=50)
    Rno=models.CharField(max_length=6)
    Emp=models.CharField(max_length=15)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)


