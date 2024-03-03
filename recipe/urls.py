from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

#Provided by djangorestframework,uses with apiview to automatically create root for all of the option avaliable for the view 
router = DefaultRouter()
# router.register('tags', views.TagViewSet)
# router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]