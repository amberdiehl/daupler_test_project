from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('teams/', TeamList.as_view(), name='team_list'),
    path('team/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
    path('roles/', RoleList.as_view(), name='role_list'),
    path('role/<int:pk>/', RoleDetail.as_view(), name='role_detail'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
