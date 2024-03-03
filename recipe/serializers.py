from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
  
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes',
            'price', 'link'
        ]
        read_only_fields = ('id',)

"""
why? - RecipeDetailSerializer is extension of the RecipeSerializer,
 take all of the functionality of RecipeSerializer and 
 add some extra field for detail serializer
"""
class RecipeDetailSerializer(RecipeSerializer):

    class Meta(RecipeSerializer.Meta):
        fields= RecipeSerializer.Meta.fields + ['description']