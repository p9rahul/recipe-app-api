from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

#Error if not override : Write an explicit .create(), update() method for serializer
class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    tags = TagSerializer(many=True, required=False) #for create -> Lis of tags assign to recipe see json
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes',
            'price', 'link','tags','ingredients',
        ]
        read_only_fields = ('id',)

    #Private mehtod ->  methods start with _ then use for internal only -> can't call this method 
    def _get_Or_Create_tags(self, tags, recipe):
        """Get method for Tags API"""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created =Tag.objects.get_or_create(
                user= auth_user,
                **tag, #name=tag['name] as of now model is having one field , but in future it may be added
            )
            recipe.tags.add(tag_obj)

    #Private mehtod 
    def _get_Or_Create_ingredients(self, ingredients, recipe):
        """Get method for ingredient API"""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created =Ingredient.objects.get_or_create(
                user= auth_user,
                **ingredient, #name=tag['name] model has one field , but in future it may be added
            )
            recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):
        """create a recipe override create method"""
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_Or_Create_tags(tags, recipe)
        self._get_Or_Create_ingredients(ingredients, recipe)

        return recipe
        
    #updating tags and ingredients to the recipe
    def update(self, instance, validated_data):
        tags= validated_data.pop('tags',None)
        ingredients = validated_data.pop('ingredients', None)
        if tags is not None:
            instance.tags.clear()
            self._get_Or_Create_tags(tags,instance)
        if ingredients is not None:
            instance.ingredients.clear()
            self._get_Or_Create_ingredients(ingredients, instance)

        for attr1, value in validated_data.items():
            setattr(instance, attr1, value)
        
        instance.save()
        return instance
        

"""
why? - RecipeDetailSerializer is extension of the RecipeSerializer,
 take all of the functionality of RecipeSerializer and 
 add some extra field for detail serializer
"""
class RecipeDetailSerializer(RecipeSerializer):

    class Meta(RecipeSerializer.Meta):
        fields= RecipeSerializer.Meta.fields + ['description']



