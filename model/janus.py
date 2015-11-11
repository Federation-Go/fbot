from base import Base
import json

m={
	'authorize':['post','/authorize'],
	'link':['post','/users/me/credentials'],
	'unlink':['post','/users/me/credentials/%(credential)s/unlink']
		}
model=Base('auth',m)




