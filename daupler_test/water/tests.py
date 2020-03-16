from collections import OrderedDict
from django.contrib.auth.models import User
from .models import Team, Role, Employee
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class TeamCreateTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('test_user', email='noemail@nowhere.com', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.data = {'name': 'Awesome Test Team'}
        self.response_data = {'id': 1, 'name': 'Awesome Test Team', 'members': []}

    def test_create_team(self):

        response = self.client.post('/teams/', self.data)

        self.assertEqual(response.status_code, 201)  # assert created
        self.assertEqual(response.data, self.response_data)  # assert result returned with new team, no members


class TeamListTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('test_user', email='noemail@nowhere.com', password='test_password')
        self.team = Team.objects.create(name='Emergency Services Test Team')
        self.role = Role.objects.create(name='Test Supervisor Role')
        Employee.objects.create(first_name='Barney', last_name='Rubble', team=self.team, role=self.role,
                                on_call_order=5)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.response_data_dict = OrderedDict()
        self.response_data_dict['id'] = 1
        self.response_data_dict['name'] = 'Emergency Services Test Team'
        self.response_data_dict['members'] = ['Rubble, Barney']
        self.response_data = [self.response_data_dict]

    def test_list_team(self):

        response = self.client.get('/teams/')

        self.assertEqual(response.status_code, 200)  # assert created
        self.assertEqual(response.data, self.response_data)  # assert result returned with team name and 1 member
