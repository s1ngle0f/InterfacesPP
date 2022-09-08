import pprint
import twitchAPI
from twitchAPI import Twitch
import requests

client_id = 'unqn1ywwwblsl0d7xrd4m1k83r1ixj'
secret_key = 'e83aj23g2gvu5nh70u9n2zy13khnef'
twitch = Twitch(client_id, secret_key)
none_sort = twitch.get_streams(first=5, language='ru')
print(none_sort)

d = {}

for streamer in none_sort['data']:
    # d[streamer['user_name']] = twitch.channel
    d[streamer['user_name']] = twitch.get_users(streamer['user_id'], streamer['user_login'])

# pprint.pprint(d)

# test = {'broadcaster_type': 'partner',
#                    'created_at': '2014-07-30T12:03:35Z',
#                    'description': 'Ex-Pro Dota2 Player',
#                    'display_name': 'Nix',
#                    'id': '67708794',
#                    'login': 'nix',
#                    'offline_image_url': 'https://static-cdn.jtvnw.net/jtv_user_pictures/aeaddfba-ec81-4716-ab3b-a8a38ca018ac-channel_offline_image-1920x1080.jpeg',
#                    'profile_image_url': 'https://static-cdn.jtvnw.net/jtv_user_pictures/c8ff98b9-b235-47c1-8079-ad10f5099dc2-profile_image-300x300.png',
#                    'type': '',
#                    'view_count': 18701734}
# tup = (1, 2, 3)

def cut_json(json, *fields):
    new_json = {}
    for k, v in json.items():
        if k in fields:
            new_json[k] = v
    return new_json

def cut_json_arr(arr, *fields):
    new_arr = []
    for json in arr:
        new_arr.append(cut_json(json, *fields))
    return new_arr

pprint.pprint(cut_json_arr(none_sort['data'], 'viewer_count', 'user_name'))
pprint.pprint(cut_json(none_sort['data'][0], 'viewer_count', 'user_name'))