from django.test import TestCase
from rest_framework.test import APIRequestFactory

import factories
from silo.api import TolaUserViewSet


class TolaUserListViewsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.hikaya_user = factories.TolaUser()

        self.hikaya_user_ringo = factories.TolaUser(
            user=factories.User(first_name='Ringo', last_name='Starr'),
            organization=self.hikaya_user.organization)
        self.hikaya_user_george = factories.TolaUser(
            user=factories.User(first_name='George', last_name='Harrison'),
            organization=factories.Organization(name='Other Org'))

    def test_list_hikayauser_superuser(self):
        self.hikaya_user.user.is_staff = True
        self.hikaya_user.user.is_superuser = True
        self.hikaya_user.user.save()

        request = self.factory.get('')
        request.user = self.hikaya_user.user
        view = TolaUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        for i, name in enumerate((u'Thom Yorke', u'Ringo Starr',
                                  u'George Harrison')):
            self.assertEqual(response.data[i]['name'], name)

    def test_list_hikayauser_other_user(self):
        request = self.factory.get('')
        request.user = self.hikaya_user.user
        view = TolaUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        for i, name in enumerate((u'Thom Yorke', u'Ringo Starr')):
            self.assertEqual(response.data[i]['name'], name)
