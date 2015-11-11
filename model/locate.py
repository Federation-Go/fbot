import requests

def locate(pandora, service):
    try:
    	url=requests.get('http://%s/locate/%s' % (pandora,service)).text
    except Exception,e:
    	raise Exception('visit pandora error!')
    return url