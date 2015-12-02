import requests,functools
import locate

class Base(object):
	def __init__(self,model,m):
		self.model=model
  		self.m=m

	def __getattr__(self,name):
		if name in self.m:
			return functools.partial(self.request,name)
		else:
			raise AttributeError
	def request(self,name,pandora,*args,**kwargs):
		url=locate.locate(pandora,self.model)
		method,addr=self.m[name]
		addr=addr % kwargs
		url='https://%s%s' % (url,addr)
		req=requests.Request(method,url,params=kwargs)
		r=req.prepare()
		s=requests.Session()
		return s.send(r)
