
from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
from . import views


router= routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('home', views.home, name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
