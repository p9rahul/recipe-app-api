from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
    Ingredient
    )
from recipe import serializers

#import mixins to add addiitonal functonality 

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

"""
# Here TagViewset and IngredientViewset has similar lines of code -> refactor
- inherit in child class"""
class BaseRecipeAttributeViewSet(
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

    # overide get_queryset to filter this viewSet to authenticated user 
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

#for info go inside each class and check method, Here CURD implement seprately
# to update tag only add UpdateModelMixin
# To delete tag model ->inherit from above class
class TagViewset(BaseRecipeAttributeViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    
#IngredientViewset ->inherit from above class
class IngredientViewset(BaseRecipeAttributeViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    