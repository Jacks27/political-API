import json
import unittest

from app.test.base_test import PoliticoV1BaseTest 

class PoliticoCandidateTeat(PoliticoV1BaseTest):
    def test_candidate_save(self):
        response= self.client().post('/api/v1/candidates', data= self.add_candidate, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    