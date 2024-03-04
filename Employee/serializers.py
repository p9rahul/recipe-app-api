from rest_framework import serializers
from core.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serialize a Employee"""
  
    class Meta:
        model = Employee
        fields = ['id','empName','gender','empAddress','department']
        read_only_fields = ('id',)