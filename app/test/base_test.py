import json

from app import create_app
import unittest


class PoliticoV1BaseTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        # tear down tests
        self.add_candidate = json.dumps({         
            'office':"1",
            'party':'1',
            'candidate': "1",
             
        })

        self.add_party = json.dumps({         
            'party_id':"1",
            'name':'ADS',
            'hqAddress': "nai",
            'logoUrl': "cbc" 
        })
        self.update_office = json.dumps({
            'name':'Adfd',
            'hqAddress': "naks",
            'logoUrl': "rsdds" 
        })
        self.empty_party_name = json.dumps({
            'name':'',
            'hqAddress': "naks",
            'logoUrl': "rsdds" 
        })
        self.empty_Adress = json.dumps({
            'name':'dff',
            'hqAddress': " ",
            'logoUrl': "rsdds" 
        })
        self.empty_logourl = json.dumps({
            'name':'qw',
            'hqAddress': "naks",
            'logoUrl': "" 
        })
        self.add_office = json.dumps({
            'name':'Adfd',
            'office_type': "naks"
            
        })

    def tearDown(self):
        """Teardown tests"""
        self.app.testing = False
        
if __name__ == "__main__":
    unittest.main()

