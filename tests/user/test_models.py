from rest_framework.test import APITestCase
from model_mommy import mommy
from helloworld.user.models import (
    User
)


class TestUserModel(APITestCase):
    def test_str(self):
        user = mommy.make(User, email="hello@world.com")
        assert str(user) == "hello@world.com"

    def test_full_name(self):
        user = mommy.make(User, first_name="hello", last_name="world")
        assert user.get_fullname() == "hello world"
