import requests,functools
from locate import locate

class Base(object):
	def __init__(self,model,m):
		self.model=model
  		self.map=m

	def __getattr__(self,name):
		if name in self.map:
			return functools.partial(self.request,name=name)
		else:
			raise AttributeError
	def request(name,pandora,*args,**kwargs):
		url=locate(pandora,self.model)
		method,addr=self.map[name]
		addr=addr%kwargs
		url='https://%s%s' % (url,addr)
		r=requests.Request(method,url,params=kwargs)
		return r