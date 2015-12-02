import json
from base import Base
m={
	'set_profile':['post','/profiles/%(credential)s/myprofile/%(selector)s'],
	'get_profile':['get','/profiles/%(credential)s/myprofile'],
	'delete_profile':['post','/profiles/%(credential)s/myprofile/delete'],
	'get_matches':['get','/profiles/matchers/%(name)s/matches'],
	'create_matcher':['post','/profiles/matchers/%(name)s'],
	'list_matchers':['get','/profiles/matchers'],
	'delete_matcher':['post','/profiles/matchers/%(name)s/delete'],
	'get_near_me_profile':['get','/profiles/location/%(credential)s']
		}
model=Base('storage',m)