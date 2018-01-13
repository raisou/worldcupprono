from datetime import timedelta

from freezegun import freeze_time
from django.utils import timezone
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from worldcupprono.factories import UserFactory

from .factories import (MatchFactory, PronoFactory)


class MatchAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory.create()

    def test_anonymous_list_matchs(self):
        response = self.client.get(reverse('matchs'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_list_matchs(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('matchs'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create_match(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(reverse('matchs'), {})

        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class PronoAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory.create()

    def test_anonymous_list_pronos(self):
        response = self.client.get(reverse('pronos-list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_list_pronos(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('pronos-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_only_his_own_pronos(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        PronoFactory.create(user=self.user, match=match)
        PronoFactory.create(user=UserFactory.create(), match=match)

        response = self.client.get(reverse('pronos-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_create_prono(self):
        match = MatchFactory.create()

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': match.id
        }

        response = self.client.post(reverse('pronos-list'), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_create_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': match.id
        }

        response = self.client.post(reverse('pronos-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('match'), match.id)
        self.assertEqual(response.data.get('score_domicile'), 0)
        self.assertEqual(response.data.get('score_visitor'), 0)

    def test_anonymous_get_specific_prono(self):
        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        response = self.client.get(reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_get_specific_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(user=self.user, match=match)

        response = self.client.get(reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_only_his_own_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        response = self.client.get(reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_update_specific_prono(self):
        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': prono.match.id
        }

        response = self.client.put(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_update_specific_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(user=self.user, match=match)

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': prono.match.id
        }

        response = self.client.put(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_only_his_own_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': prono.match.id
        }

        response = self.client.put(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_partial_update_specific_prono(self):
        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        data = {
            'score_domicile': 0
        }

        response = self.client.patch(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_partial_update_specific_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(user=self.user, match=match)

        data = {
            'score_domicile': 0
        }

        response = self.client.patch(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_partial_update_his_own_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        data = {
            'score_domicile': 0
        }

        response = self.client.patch(
            reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_delete_prono(self):
        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        response = self.client.delete(
            reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_delete_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(user=self.user, match=match)

        response = self.client.delete(
            reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_delete_his_own_prono(self):
        self.client.force_authenticate(user=self.user)

        match = MatchFactory.create()
        prono = PronoFactory.create(match=match)

        response = self.client.delete(
            reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_update_prono_after_time(self):
        self.client.force_authenticate(user=self.user)

        match_date = timezone.now()
        match = MatchFactory.create(date=match_date)
        prono = PronoFactory.create(user=self.user, match=match)

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': match.id
        }

        with freeze_time(match_date - timedelta(days=1, hours=2)):
            response = self.client.put(
                reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with freeze_time(match_date - timedelta(days=1)):
            response = self.client.put(
                reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with freeze_time(match_date - timedelta(hours=23, minutes=59)):
            response = self.client.put(
                reverse('pronos-detail', args=[prono.id]), data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete_prono_after_time(self):
        self.client.force_authenticate(user=self.user)

        match_date = timezone.now()
        match = MatchFactory.create(date=match_date)
        prono = PronoFactory.create(user=self.user, match=match)

        with freeze_time(match_date - timedelta(hours=23)):
            response = self.client.delete(
                reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        with freeze_time(match_date - timedelta(hours=25)):
            response = self.client.delete(
                reverse('pronos-detail', args=[prono.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_create_prono_after_time(self):
        self.client.force_authenticate(user=self.user)

        match_date = timezone.now()
        match = MatchFactory.create(date=match_date)

        data = {
            'score_domicile': 0,
            'score_visitor': 0,
            'match': match.id
        }

        with freeze_time(match_date - timedelta(hours=23)):
            response = self.client.post(reverse('pronos-list'), data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
