from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from teams.models.team import TeamModel
from teams.models.person import PersonModel


class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = TeamModel.objects.create(name='Test Team')
        self.person = PersonModel.objects.create(first_name='Test', last_name='Test', email='test@test.com')

    def test_create_person(self):
        data = {'first_name': 'Test2', 'last_name': 'Test2', 'email': 'test2@test.com'}
        response = self.client.post(path='/persons/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PersonModel.objects.count(), 2)

    def test_get_person(self):
        response = self.client.get(path=f'/persons/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@test.com')

    def test_create_team(self):
        data = {'name': 'New Team'}
        response = self.client.post(path='/teams/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TeamModel.objects.count(), 2)

    def test_get_team(self):
        response = self.client.get(path=f'/teams/{self.team.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Team')

    def test_add_team_member(self):
        response = self.client.post(path=f'/teams/{self.team.id}/add_member/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_team_member(self):
        response = self.client.post(path=f'/teams/{self.team.id}/remove_member/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_not_existing_team(self):
        response = self.client.get(path=f'/teams/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_not_existing_person(self):
        response = self.client.get(path=f'/persons/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
