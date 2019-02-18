import json
import unittest

from app.test.base_test import PoliticoV1BaseTest


class PoliticalTests(PoliticoV1BaseTest):
    """Tests functionality of the political endpoint"""

    def test_create_users(self):
        """Test API can create a party"""
        response = self.client().post('/api/v2/signup', data=self.success_signup,
        content_type='application/json')

        self.assertEqual(response.status_code, 201)

  