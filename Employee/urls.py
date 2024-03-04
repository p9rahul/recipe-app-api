from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Employee import views

#Provided by djangorestframework,uses with apiview to automatically create root for all of the option avaliable for the view 
router = DefaultRouter()
router.register('Employee', views.EmployeeViewSet)

app_name = 'Employee'

urlpatterns = [
    path('', include(router.urls))
]