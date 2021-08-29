# Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить кто самый умный(intelligence) 
# из трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name

# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
superheroes = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]

for hero in superheroes:
  sup_hero = requests.get(url + hero['name'])
  hero['intelligence'] = int(sup_hero.json()['results'][0]['powerstats']['intelligence'])
    
print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])