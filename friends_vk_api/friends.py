import requests
import json
import datetime

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
V = '5.71'
YEAR = datetime.datetime.now().year

def calc_age(uid):
	#Service key for accessing

	friends_age = dict()

	url = 'https://api.vk.com/method/friends.get'

	user_id = get_ID(uid)
	req = requests.get(url, params={
		'access_token': ACCESS_TOKEN,
		'user_id': user_id,
		'v': V,
		'fields': 'bdate'
	})

	text_d = json.loads(req.text)

	friends = text_d['response']['items']

	for friend in friends:
		if 'bdate' in friend:
			if len(friend['bdate'].split('.')) == 3:
				bdate = YEAR - int(friend['bdate'].split('.')[2])
				if bdate not in friends_age:
					friends_age[bdate] = 1
				else:
					friends_age[bdate] += 1

	friends_age = list(friends_age.items())

	return sorted(friends_age, key=lambda x: (-x[1], x[0]))

def get_ID(uid):
	url = 'https://api.vk.com/method/users.get'

	req = requests.get(url, params={
		'access_token': ACCESS_TOKEN,
		'user_ids' : uid,
         'v': V
	})

	text_d = json.loads(req.text)
	return text_d['response'][0]['id']

if __name__ == '__main__':
	res = calc_age('alexey_absurd')
	print(res)
