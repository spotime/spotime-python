import mock, unittest
from spotime import http_client
from utils import SpotimeMockRequest

class TestHttpClient(unittest.TestCase):
    def setUp(self):
        pass
	
    def test_http_client_init(self):
        url = 'api/v1/coworkers'
 	client = http_client.HttpClient(username="foo", password="bar")
        self.assertEqual(client.password, "bar")
        self.assertEqual(client.username, "foo")

    def test_http_client_request_with_basic_auth(self):
       url = 'api/v1/coworkers'
       http_client.urllib2.Request = mock.Mock(return_value=SpotimeMockRequest())
       http_client.urllib2.urlopen = mock.Mock(return_value="FOOBAR")
       client = http_client.HttpClient(username="foo", password="bar")
       result = client.request(url, use_auth=True)
       self.assertEqual(result, "FOOBAR")

if __name__ == '__main__':
    unittest.main()
