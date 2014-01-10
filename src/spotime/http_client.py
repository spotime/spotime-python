import urllib2, base64

class HttpClient(object):
    BASE_URL = 'http://something.net/{0}'
    def __init__(self, url, *args, **kwargs):
    """
    *args is for extra positional argumets that you didn't account for and **kwargs are for extra keyword arguments that you didn't account for
				this way if someone is stupid and calls your clas like HttpClient(foo bar, one=two) it won't crash
				but it has other uses too which you'll see later on

				"""
						self.url = url
 
				def request(use_auth=False, user_name=None, password=None, *args, **kwargs):
						request = urllib2.Request(BASE_URL.format(self.url))
      if use_auth:
          if not user_name or not password:
												raise Exception("Please make sure add the username and password when using Auth")
          base64string = base64.ecodestring('{0}:{1}'.format(user_name, password).replace('\n',''))
          request.add_header("Authorization", "Basic {0}".format(base64string))
      result = urlib2.urlopen(request)
      return result
