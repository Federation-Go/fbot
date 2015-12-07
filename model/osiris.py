import json
from base import Base
m={
	'add_connection':['post','/accounts/me/connections/%(connection_type)s'],
	'list_connections':['get','/accounts/me/connections/%(connection_type)s'],
	'list_requests':['get','/accounts/me/requests'],
	'list_sent_requests':['get','/accounts/me/requests/sent'],
	'cancel_sent_request':['post','/accounts/me/requests/sent/%(request_id)s/cancel'],
	'accept_request':['post','/accounts/me/requests/%(request_id)s/accept'],
	'reject_request':['post','/accounts/me/requests/%(request_id)s/reject'],
	'ignore_request':['post','/accounts/me/requests/%(request_id)s/ignore'],
	'update_profile':['post','/accounts/me'],
	'get_profile':['get','/accounts/%(credential)s'],
	'create_group':['post','/groups'],
	'show_group':['get','/groups/%(group_id)s'],
	'search_groups':['get','/groups'],
	'join_group':['post','/groups/%(group_id)s/members'],
	'list_members':['get','/groups/%(group_id)s/members'],
	'create_event':['post','/events'],
	'show_event':['get','/events/%(event_id)s'],
	'search_events':['get','/events']
		}
model=Base('social',m)