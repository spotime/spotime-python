import mock, unittest
from spotime import http_client
from utils import SpotimeMockRequest

class TestHttpClient(unittest.TestCase):
    def setUp(self):
				    pass

		  def test_http_client_init(self):
 							url = 'api/v1/coworkers'
 							http_client = http_client.HttpClient(url)
 							self.assertEqual(http_client, 'http://something.net/{0}'.format(url))

    def test_http_client_request_with_basic_auth(self):
 					  url = 'api/v1/coworkers'
 							"now the mocking begins :)"
 							http_client.urllib2.Request = mock.Mock(return_value=SpotimeMockRequest)
        http_client.urllib2.urlopen = Mock(return_value="FOOBAR")

 							client = http_client.HttpClient(url)
 							result = client.request(use_auth=True, user_name="one", password="two")
 							self.assertEqual(result, "FOOBAR")
if __name__ == '__main__':
    unittest.main()
