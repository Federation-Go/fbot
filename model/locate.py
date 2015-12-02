import requests
import urlparse 
pandora_url={}
def locate(pandora, service):
    try:
        p=urlparse.urljoin(pandora,"locate/%s" %service)
    	url=requests.get(p).text
    	global pandora_url
    	pandora_url[pandora] = url
    except Exception,e:
    	raise Exception('visit pandora error!')
    return url
