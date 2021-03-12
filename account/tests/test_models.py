from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_new_user_with_email_successful(self):
        email = 'mansour@datamid.my'
        password = 'Test102030'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        email = 'mansour@DATAMIND.MY'
        password = 'Test10203040'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email.lower())

    def test_create_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test10203040')

    def test_create_superuser_with_email(self):
        email = 'admin@DATAMIND.MY'
        password = 'Test10203040'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email.lower())
        self.assertTrue(user.check_password(password))


