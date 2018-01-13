from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from worldcupprono.factories import UserFactory
from pronos.factories import (MatchFactory, PronoFactory)

from .factories import BoardFactory


class BoardAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory.create()

    def test_anonymous_list_boards(self):
        response = self.client.get(reverse('boards-list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_list_boards(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('boards-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_his_own_boards(self):
        self.client.force_authenticate(user=self.user)

        BoardFactory.create(owner=self.user)
        BoardFactory.create()

        response = self.client.get(reverse('boards-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_create_board(self):
        data = {
            'name': 'foo'
        }

        response = self.client.post(reverse('boards-list'), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_create_board(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'foo'
        }

        response = self.client.post(reverse('boards-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), data.get('name'))

    def test_anonymous_get_specific_board(self):
        board = BoardFactory.create()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_get_specific_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_only_his_own_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_update_specific_board(self):
        board = BoardFactory.create()

        data = {
            'name': 'foobar'
        }

        response = self.client.put(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_update_specific_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)

        data = {
            'name': 'foobar'
        }

        response = self.client.put(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_only_his_own_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create()

        data = {
            'board': 'foobar'
        }

        response = self.client.put(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_partial_update_specific_board(self):
        board = BoardFactory.create()

        data = {
            'name': 'foo'
        }

        response = self.client.patch(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_partial_update_specific_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)

        data = {
            'name': 'foo'
        }

        response = self.client.patch(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_partial_update_his_own_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create()

        data = {
            'name': 'foo'
        }

        response = self.client.patch(
            reverse('boards-detail', args=[board.id]), data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_anonymous_delete_board(self):
        board = BoardFactory.create()

        response = self.client.delete(
            reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_delete_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)

        response = self.client.delete(
            reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_delete_his_own_board(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create()

        response = self.client.delete(
            reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cant_see_others_boards_if_not_invited(self):
        self.client.force_authenticate(user=self.user)

        user2 = UserFactory.create()
        board = BoardFactory.create(owner=user2)

        response = self.client.get(
            reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('boards-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_anonymous_invite_board(self):
        pass

    def test_user_invite_board(self):
        pass

    def test_user_invite_on_his_own_boards(self):
        pass

    def test_user_invite_unknown_user_send_mail(self):
        pass

    def test_user_invite_known_auto_add_board(self):
        pass

    def test_score_user_exact(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)
        match = MatchFactory.create()
        prono = PronoFactory.create(user=self.user, match=match)

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)

        # now validate match score
        match.score_domicile = prono.score_domicile
        match.score_visitor = prono.score_visitor
        match.played = True
        match.save()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 3)

    def test_score_user_partial(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)
        match = MatchFactory.create()
        prono = PronoFactory.create(
            score_domicile=1, score_visitor=0, user=self.user, match=match)

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)

        # now validate match score
        match.score_domicile = 2
        match.score_visitor = prono.score_visitor
        match.played = True
        match.save()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 1)

    def test_score_user_wrong(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)
        match = MatchFactory.create()
        prono = PronoFactory.create(
            score_domicile=1, score_visitor=0, user=self.user, match=match)

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)

        # now validate match score
        match.score_domicile = prono.score_visitor
        match.score_visitor = prono.score_domicile
        match.played = True
        match.save()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)

    def test_score_user_if_no_prono(self):
        self.client.force_authenticate(user=self.user)

        board = BoardFactory.create(owner=self.user)
        match = MatchFactory.create()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)

        # now validate match score
        match.score_domicile = 0
        match.score_visitor = 0
        match.played = True
        match.save()

        response = self.client.get(reverse('boards-detail', args=[board.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users')[0].get('points'), 0)
