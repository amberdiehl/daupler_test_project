from django.contrib import admin
from .models import Team, Role, Employee


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'team', 'role', 'on_call_order', )
