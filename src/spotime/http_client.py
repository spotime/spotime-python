import urllib, urllib2, base64

class HttpClient(object):

    BASE_URL = 'http://spoti.me/api/v1/{0}'

    def __init__(self, apiKey=None, apiId=None, *args, **kwargs):
        """
            *args is for extra positional argumets that you didn't account for and **kwargs are for extra keyword arguments that you didn't account for this way if someone is stupid and calls your clas like HttpClient(foo bar, one=two) it won't crash but it has other uses too which you'll see later on
        """
        self.apiKey = apiKey
        self.apiId = apiId 
        
        if not self.apiKey or not self.apiId:
            raise Exception("Please make sure add the username and password when using Auth")

    def request(self, url, post=False, params=None, *args, **kwargs):
        data = dict()
        if params:
            data = urllib.urlencode(params)
        
        if post:
            url = HttpClient.BASE_URL.format(url)
            print '...............', url
            request = urllib2.Request(url, data)
        else:
            url = '{0}?{1}'.format(HttpClient.BASE_URL.format(url), data)
            request = urllib2.Request(url)
       
        base64string = base64.encodestring('{0}:{1}'.format(self.apiId, self.apiKey).replace('\n',''))
        request.add_header("Authorization", "Basic {0}".format(base64string))      
 
        result = urllib2.urlopen(request)
        return result.read()#this is not clean we need to add in exception handling

if __name__ == '__main__':
    #let's test out a POST call
    client = HttpClient(username='iphone', password='secret')
    response = client.request('coworkers/', post=True, params=dict(name='jon', email='sam@webiken.net', password='superawesomepass12', accept_terms=True))
    print response
    response = client.request('coworkers')
    print response
