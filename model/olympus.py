import json
from base import Base
m={
	'top_entries':['get','/leaderboards/%(sort)s/%(name)s'],
	'entries_around_me':['get','/leaderboards/%(sort)s/%(name)s/%(credential)s'],
	'retrieve_friend_leaderboard':['get','/leaderboards/%(sort)s/%(name)s/me/friends'],
	'retrieve_location_leaderboard':['get','/leaderboards/%(sort)s/%(name)s/me/location'],
	'list_leaderboards':['get','/leaderboards/%(sort)s'],
	'post_entry':['post','/leaderboards/%(sort)s/%(name)s/me'],
	'delete_entry':['post','/leaderboards/%(sort)s/%(name)s/me/delete'],
	'clear_leaderboard':['post','/leaderboards/desc/%(name)s/clear'],
	'create_league_leaderboard':['post','/leaderboards/%(sort)s/%(name)s/settings'],
	'create_tiered_leaderboard':['post','/leaderboards/%(sort)s/%(name)s/settings']
		}
model=Base('leaderboard',m)