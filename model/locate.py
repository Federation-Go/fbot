import requests
import urlparse 

def locate(pandora, service):
    try:
        p=urlparse.urljoin(pandora,"locate/%s" %service)
    	url=requests.get(p).text
    except Exception,e:
    	raise Exception('visit pandora error!')
    return url
