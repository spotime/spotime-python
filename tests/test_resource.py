import unittest, mock
from StringIO import StringIO

from spotime import http_client
from spotime.resource import Coworker

from utils import SpotimeMockRequest

class TestResources(unittest.TestCase):


    def test_retrive_call_coworkers(self):
        http_client.urllib2.Request = mock.Mock(return_value=SpotimeMockRequest())     

        http_client.urllib2.urlopen = mock.Mock(return_value=StringIO("""[{"email":"testing@webiken.net", "password":"password1", "name":"John Smith"}]"""))
        coworker = Coworker.all(apiKey='foo', apiId='bar')
        self.assertEqual(coworker.email, 'testing@webiken.net')
        self.assertEqual(coworker.password, 'password1')
        self.assertEqual(coworker.name, 'John Smith') 



if __name__ == '__main__':
    unittest.main()
