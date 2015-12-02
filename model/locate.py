import requests
import urlparse 
from collections import defaultdict

pandora_url=defaultdict(dict)

def locate(pandora, service):
    try:
    	if pandora in pandora_url and service in pandora_url[pandora]:
    		return pandora_url[pandora][service]
        p=urlparse.urljoin(pandora,"locate/%s" %service)
    	url=requests.get(p).text
    	pandora_url[pandora][service]=url
    except Exception,e:
    	raise Exception('visit pandora error!')
    return url
