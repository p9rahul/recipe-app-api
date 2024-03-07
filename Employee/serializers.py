from rest_framework import serializers
from core.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serialize a Employee"""
  
    class Meta:
        model = Employee
        fields = ['id','empName','gender','empAddress','department']
        read_only_fields = ('id',)

    
    # - We can write a different class for validation and inherit in model sterilizer class
    # - In the class also ex - def method
    # - Validate Gender doesn't contain either M or F -> this can be pass in model class as choices
    def validate(self, data):
        
        if data['empName']:
            for n in data['empName']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': 'Name cannot be numeric'})
                
    
                
        return data