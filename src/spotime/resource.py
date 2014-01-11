import simplejson

from http_client import HttpClient

def _populate_spotime_object(response, *args, **kwargs):
    _data = simplejson.loads(response)
    return _data


class SpotimeObject(object):

     def __init__(self, *args, **kwargs):
         if 'attrs' in kwargs:
              attrs = kwargs.get('attrs')
              for attr in attrs:
                  self.__setattr__(attr, kwargs.get(attr))     
              print '...........', self.__dict__
     @classmethod
     def call(cls, url, apiId, apiKey, data=None, post=False, *args, **kwargs):
         """
              to use the library, we import spotime

              import spotime
              spotime.apiId = 'foo'
              spotime.apiKey = 'bar'

              spotime.Coworker.all(username='sam', password='bar')
              
              and inside all we call the SpotimeObject.call method and give it the right url and parameters
              design decisions:  in the SpotimeObject.call we need to pass the params and url
         """
         client = HttpClient(apiId=apiId, apiKey=apiKey)
         response = client.request(url, post=post, data=data)
         json = _populate_spotime_object(response)
         if len(json) == 1:
             return cls(**json[0])
         return [cls(**_kwargs) for _kwargs in json]
           


class Coworker(SpotimeObject):


    def __init__(self, *args, **kwargs):
        attrs = ('email', 'name', 'password',)
        super(Coworker, self).__init__(*args, attrs=attrs, **kwargs)
        """now we take the things that relate to a coworker"""

    @classmethod
    def all(cls, apiId, apiKey, *args, **kwargs):
        """ here we need to call the httprequest and po
        """
        return cls.call('coworkers', apiId, apiKey)

    def __unicode__(self):
        return "My name is {0} and my email is {1}".format(self.name, self.email)
