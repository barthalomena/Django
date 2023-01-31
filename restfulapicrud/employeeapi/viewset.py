from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.all()
    serializer_class=serializers.EmployeeSerializers

    # viewsets=>list/retrive/create/update/destroy


