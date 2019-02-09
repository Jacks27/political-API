import json
import unittest

from app.test.base_test import PoliticoV1BaseTest


class PoliticalTests(PoliticoV1BaseTest):
    """Tests functionality of the political endpoint"""

    def test_create_party(self):
        """Test API can create a party"""
        response = self.client().post('/v1/views/party', data=self.add_party,
        content_type='application/json')

        self.assertEqual(response.status_code, 201)

    # def test_get_all_parties(self):
    #     """Tests API can get all parties"""
    #     parties = {"parties": "parties"}
    #     response = self.client().get('/api/v1/all_parties', data=parties,
    #                                  content_type='application/json')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_specific_party(self):
    #     """Tests API can get a specific party by using its id"""
    #     self.client().post('/api/v1/party', data=self.add_party,
    #                        content_type='application/json')
    #     response = self.client().get('/api/v1/get_party/1',
    #                                  content_type='application/json',
    #                                  )
    #     self.assertEqual(response.status_code, 200)

    # def test_wrong_political_party_id(self):
    #     self.client().post('/api/v1/party', data=self.add_party,
    #                        content_type='application/json')
    #     response = self.client().get('/api/v1/get_party/10',
    #                                  content_type='application/json',
    #                                  )
    #     self.assertEqual(response.status_code, 404)

    # def test_party_updated(self):
    #     self.client().post('/api/v1/party', data=self.add_party,
    #                        content_type='application/json')
    #     response = self.client().patch('/api/v1/party/1', data=self.update_office,
    #                                  content_type='application/json',
    #                                  )
    #     self.assertEqual(response.status_code, 200)

    #     response = self.client().patch('/api/v1/update_party/6', data=self.update_office,
    #                                  content_type='application/json',
    #                                  )
    #     self.assertEqual(response.status_code, 404)

    # def test_delete_party_by_id(self):
    #     """Tests endpoint can delete one by using its id"""

    #     response = self.client().delete('/api/v1/remove_party/1',
    #                                     content_type='application/json',
    #                                     )
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_non_existing_party(self):
    #     response = self.client().delete('/api/v1/remove_party/4',
    #                                     content_type='application/json',
    #                                     )
    #     self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()