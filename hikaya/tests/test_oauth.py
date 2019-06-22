from django.test import TestCase

import factories
from hikaya import auth_pipeline
from silo.models import HikayaUser
from django.contrib.auth.models import User

# TODO Extend OAuth tests


class BackendTest(object):
    def __init__(self):
        self.USER_FIELDS = ['username', 'email']

    def setting(self, name, default=None):
        return self.__dict__.get(name, default)


class UserOAuthTest(object):
    def username_max_length(self):
        return 1000


class StorageTest(object):
    def __init__(self):
        self.user = UserOAuthTest()


class StrategyTest(object):
    def __init__(self):
        self.CLEAN_USERNAMES = False
        self.storage = StorageTest()

    def setting(self, name, default=None):
        return self.__dict__.get(name, default)


class OAuthTest(TestCase):
    """
    Test cases for OAuth Provider interface
    """

    def setUp(self):
        self.hikaya_user = factories.TolaUser()
        self.org = factories.Organization()
        self.country = factories.Country()

    def test_user_to_hikaya_with_hikaya_user_data(self):
        response = {
            'hikaya_user': {
                'hikaya_user_uuid': '13dac835-3860-4d9d-807e-d36a3c106057',
                'name': 'John Lennon',
                'employee_number': None,
                'title': 'mr',
                'privacy_disclaimer_accepted': True,
            },
            'organization': {
                'name': self.org.name,
                'organization_uuid': self.org.organization_uuid,
            }
        }

        user = factories.User(first_name='John', last_name='Lennon')
        auth_pipeline.user_to_hikaya(None, user, response)
        hikaya_user = HikayaUser.objects.get(name='John Lennon')

        self.assertEqual(hikaya_user.name, response['hikaya_user']['name'])
        self.assertEqual(hikaya_user.organization.name, self.org.name)

    def test_user_to_hikaya_without_hikaya_user_data(self):
        # HikayaUser will be created with the default Org
        response = {
            'displayName': 'John Lennon',
            'emails': [{
                'type': 'account',
                'value': 'john.lennon@testenv.com'
            }]
        }

        user = factories.User(first_name='John', last_name='Lennon')
        auth_pipeline.user_to_hikaya(None, user, response)
        hikaya_user = HikayaUser.objects.get(user=user)

        self.assertEqual(hikaya_user.name, response.get('displayName'))
        self.assertEqual(hikaya_user.organization.name, self.org.name)
        self.assertEqual(hikaya_user.country.country, self.country.country)

        # HikayaUser will be retrieved and Org won't be the default anymore
        new_org = factories.Organization(name='New Organization')
        hikaya_user.organization = new_org
        hikaya_user.save()
        auth_pipeline.user_to_hikaya(None, user, response)
        hikaya_user = HikayaUser.objects.get(user=user)

        self.assertEqual(hikaya_user.organization.name, new_org.name)

    def test_user_to_hikaya_org_extra_fields(self):
        response = {
            'hikaya_user': {
                'hikaya_user_uuid': '13dac835-3860-4d9d-807e-d36a3c106057',
                'name': 'John Lennon',
                'employee_number': None,
                'title': 'mr',
                'privacy_disclaimer_accepted': True,
            },
            'organization': {
                'name': self.org.name,
                'url': '',
                'industry': '',
                'sector': '',
                'organization_uuid': self.org.organization_uuid,
                'chargebee_subscription_id': '',
                'chargebee_used_seats': ''
            }
        }

        user = factories.User(first_name='John', last_name='Lennon')
        auth_pipeline.user_to_hikaya(None, user, response)
        hikaya_user = HikayaUser.objects.get(name='John Lennon')

        self.assertEqual(hikaya_user.name, response['hikaya_user']['name'])
        self.assertEqual(hikaya_user.organization.name, self.org.name)

    def test_get_or_create_user_without_user(self):
        """
        We don't have a user, it will be created and returned in the
        response
        """
        strategy = StrategyTest()
        details = {
            'username': 'johnlennon'
        }
        kwargs = {
            'username': 'johnlennon',
            'email': 'john.lennon@testenv.com'
        }
        backend = BackendTest()

        response = auth_pipeline.get_or_create_user(
            strategy, details, backend, user=None, args=None, **kwargs)

        user = User.objects.get(username=details['username'])
        self.assertEqual(user.email, kwargs.get('email'))
        self.assertTrue(response['is_new'])
        self.assertEqual(response['user'].username, user.username)
        self.assertEqual(response['user'].email, user.email)
        self.assertEqual(kwargs['username'], user.username)
        self.assertEqual(kwargs['email'], user.email)

    def test_get_or_create_user_with_user(self):
        """
        As we already have a user, it will be fetched and not updated
        """
        user = factories.User()
        strategy = StrategyTest()
        details = {
            'username': user.username
        }
        kwargs = {
            'username': 'John Lennon',
            'email': 'john.lennon@testenv.com'
        }
        backend = BackendTest()

        response = auth_pipeline.get_or_create_user(
            strategy, details, backend, user=None, args=None, **kwargs)

        self.assertFalse(response['is_new'])
        self.assertEqual(response['user'].username, user.username)
        self.assertEqual(response['user'].email, user.email)
        self.assertNotEqual(kwargs['username'], user.username)
        self.assertNotEqual(kwargs['email'], user.email)
