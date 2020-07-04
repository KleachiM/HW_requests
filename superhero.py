import requests

host = 'https://www.superheroapi.com/api.php'
token = '2619421814940190'
heroes_list = ['Hulk', 'Captain America', 'Thanos']


def iq_compare(heroes_list):
    heroes_dict = dict.fromkeys(heroes_list)
    for hero in heroes_list:
        url = host + '/' + token + '/search/' + hero
        heroes_dict[hero] = int(requests.get(url).json()['results'][0]['powerstats']['intelligence'])

    max_iq = 0
    max_iq_hero = 0
    for hero in heroes_dict:
        if max_iq < heroes_dict[hero]:
            max_iq = heroes_dict[hero]
            max_iq_hero = hero

    print(f'Максимальным интеллектом {max_iq} обладает {max_iq_hero}')


iq_compare(heroes_list)