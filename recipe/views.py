from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Recipe to view or edit"""
     #here RecipeSerializer ->change-> RecipeDetailSerializer
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all() #object avliable for viewset
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.serializer_class
    
    #viewset method
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
