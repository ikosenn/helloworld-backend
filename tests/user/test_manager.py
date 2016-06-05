import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

USER_MODEL = get_user_model()


class TestUserManager(APITestCase):
    def test_create_user(self):
        """
        should create a user successfully.
        """
        user_obj = {
            'email': 'i@me.com',
            'first_name': 'Hello',
            'last_name': 'World',
            'password': 'some#$complexPass',
        }
        USER_MODEL.objects.create_user(**user_obj)

        assert USER_MODEL.objects.all().count() == 1

    def test_fails_without_email(self):
        """
        should raise a ValueError
        """
        user_obj = {
            'first_name': 'Hello',
            'last_name': 'World',
            'password': 'some#$complexPass',
        }

        with pytest.raises(ValueError) as e:
            USER_MODEL.objects.create_user(**user_obj)
        assert str(e.value) == 'Users must have an email address'

    def test_create_super_user(self):
        """
        Should create a superuser
        """
        user_obj = {
            'email': 'i@me.com',
            'first_name': 'Hello',
            'last_name': 'World',
            'password': 'some#$complexPass',
        }
        USER_MODEL.objects.create_superuser(**user_obj)

        assert USER_MODEL.objects.all().count() == 1
        assert USER_MODEL.objects.get(email='i@me.com').is_admin is True
