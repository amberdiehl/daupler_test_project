from rest_framework import serializers
from .models import Team, Role, Employee


class TeamSerializer(serializers.ModelSerializer):

    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', ]


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name', ]


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'team', 'role', 'on_call_order', ]
