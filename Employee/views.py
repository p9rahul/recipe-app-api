from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Employee
from Employee import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows employees to view or edit"""
     
    serializer_class = serializers.EmployeeSerializer
    queryset = Employee.objects.all() #object avliable for viewset
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializers.EmployeeSerializer
        
        return self.serializer_class
    
    #viewset method
    def perform_create(self, serializer):
        """Save the request at user level"""
        serializer.save(user=self.request.user)
